#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Card {
    char rank;
    char suit;
};

int cardValue(char rank) {
    switch (rank) {
        case '6': return 0;
        case '7': return 1;
        case '8': return 2;
        case '9': return 3;
        case 'T': return 4;
        case 'J': return 5;
        case 'Q': return 6;
        case 'K': return 7;
        case 'A': return 8;
    }
    return -1;
}

bool canDefeat(const Card &pisiCard, const Card &opponentCard, char trumpSuit) {
    if (pisiCard.suit == trumpSuit && opponentCard.suit != trumpSuit) {
        return true;
    }
    if (pisiCard.suit == opponentCard.suit) {
        return cardValue(pisiCard.rank) > cardValue(opponentCard.rank);
    }
    return false;
}

int main() {
    // test case amount
    int T;
    cin >> T;
    vector<bool> results;
    
    while (T--) {
        int N, M;
        char trumpSuit;
        cin >> N >> M >> trumpSuit;
        
        vector<Card> pisiCards(N);
        vector<Card> opponentCards(M);
        
        for (int i = 0; i < N; ++i) {
            cin >> pisiCards[i].rank >> pisiCards[i].suit;
        }
        
        for (int i = 0; i < M; ++i) {
            cin >> opponentCards[i].rank >> opponentCards[i].suit;
        }

        // assume pisi always win
        bool canWin = true;
        
        for (Card &opponentCard : opponentCards) {
            bool defeated = false;
            for (int i = 0; i < pisiCards.size(); i++) {
                // check if pisi can defeat the opponent card
                if (canDefeat(pisiCards[i], opponentCard, trumpSuit)) {
                    defeated = true;
                    // remove defeated card
                    pisiCards.erase(pisiCards.begin() + i);
                    break;
                }
            }
            // if cant defeat, pisi lose
            if (!defeated) {
                canWin = false;
                break;
            }
        }
        results.push_back(canWin);
        pisiCards.clear();
        opponentCards.clear();
    }
    for (int i = 0; i < results.size(); i++) {
        if (results[i]) {
            cout << "YA" << endl;
        } else {
            cout << "TIDAK" << endl;
        }
    }
    return 0;
}
