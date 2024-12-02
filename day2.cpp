#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;


int Part1() {
    // Open .csv file
    ifstream file("day2.csv");

    string line;
    vector<vector<int>> data; 

    // Grab all entries in .csv and put into a square vector for comparison
    while (getline(file, line)) {
        stringstream lineStream(line);
        vector<int> row;
        string cell;

        while (getline(lineStream, cell, ',')) {
            row.push_back(stoi(cell)); 
        }

        data.push_back(row);
    }

    file.close();

    int safe = 0;

    for (const auto& row : data) {
        
        bool isIncreasing = row[0] < row[1];
        bool isSafe = true;

        // Check all pairs in the row
        for (int j = 0; j < row.size() - 1; ++j) {
            int diff = row[j+1] - row[j];
            if ((isIncreasing && diff < 1) || (!isIncreasing && diff > -1) || abs(diff) > 3) {
                isSafe = false;
                break;
            }
        }

        // If isSafe did not change in the loop then the entry is considered safe.
        if (isSafe) {
            safe++;
        }
    }
    cout << safe << endl;
    return 0;
}



int Part2() {
    // Open .csv file
    ifstream file("day2.csv");

    string line;
    vector<vector<int>> data; 

    // Grab all entries in .csv and put into a square vector for comparison
    while (getline(file, line)) {
        stringstream lineStream(line);
        vector<int> row;
        string cell;

        while (getline(lineStream, cell, ',')) {
            row.push_back(stoi(cell)); 
        }

        data.push_back(row);
    }

    file.close();

    int safe = 0;

    for (const auto& row : data) {
        
        bool isIncreasing = row[0] < row[1];
        bool isSafe = true;
        bool Dampened = false;
        // Check all pairs in the row
        for (int j = 0; j < row.size() - 1; ++j) {
            int diff = row[j+1] - row[j];
            if ((isIncreasing && diff < 1) || (!isIncreasing && diff > -1) || abs(diff) > 3) {

                // The only thing changed in part2 is that one entry in the vector is allowed to be wrong. This is implemented using the dampened var.
                if (Dampened) {
                    isSafe = false;
                    break;
                }
                Dampened = true;
            }
        }

        // If isSafe did not change in the loop then the entry is considered safe.
        if (isSafe) {
            safe++;
        }
    }
    cout << safe << endl;
    return 0;
}


int main() {
    Part1();
    Part2();
    return 0;
}