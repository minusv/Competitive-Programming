long long A[10000001];
long long solve(int n,int seed)
{
    srand(seed);
    A[1]=1;
    long long res=0;
    for(int i=2;i<=n;i++)
    {
        int l=rand()%(i-1)+1;
        int r=rand()%(i-1)+1;
        if(l>r)
        {
            swap(l,r);
        }
        A[i]=rand()%1000000;
        for(int j=l;j<=r;j++)
        {
            A[i]=max(A[j],A[i]);
        }
        res+=A[i];
    }
    return res;
}