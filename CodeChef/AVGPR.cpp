#include<bits/stdc++.h>
using namespace std;

void check(float arr[], int n)
{
    unordered_set<float> s;
    for (int i = 0; i < n; i++)
        {s.insert(arr[i]);}
    int c=0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (s.find((arr[i] + arr[j])/2) != s.end()) {
                c++;
            }
        }
    }
    cout<<c<< endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin >> n;
        float arr[n-1];
        for(int j=0;j<n;j++)
        {
            cin>>arr[j];
        }
        check(arr,n);
    }
    return 0;
}
