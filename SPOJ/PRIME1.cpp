#include<iostream>
#include<math.h>
using namespace std;
void check(int num)
{
    int count=0;
    for(int i=2;i<=int(sqrt(num));i++)
    {
        if(num%i==0) count++;
        if(count>0) break;
    }
    if(count==0)
    {
        cout<<num<<endl;
    }
}
void prime(int *arr)
{
    int pnum[]={2,3,5,7,11,13,17,19};
    if(arr[1]<=20)
    {
        for(int i=0;i<8;i++)
        {
            if((pnum[i]>=arr[0])&&(pnum[i]<=arr[1])) cout<<pnum[i]<<endl;
        }
    }
    else
    {
        if(arr[0]%2==0)
        {
            for(int i=arr[0]+1;i<=arr[1];i=i+2)
            {
                if(i==3) cout<<2<<endl<<3<<endl;
                else check(i);
            }
        }
        else
        {
            for(int i=arr[0];i<=arr[1];i=i+2)
            {
                if(i==1) cout<<2<<endl; 
                else check(i);
            }
        }
    }
}

int main()
{
    int n;
    cin>>n;
    int arr[2];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<2;j++)
        {
            cin>>arr[j];
        }
        prime(arr);
        if(i!=n-1) cout<<endl;
    }
    return 0;
}
