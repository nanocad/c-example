/*
Array read with pointer

*/
#include <iostream>

using namespace std;

int main()
{
   int A[2][3]={1,2,3,4,5,6};
   int (*tmp)[3];
   tmp=A;
   //cout << *(tmp) << A << endl;
   for(int i=0;i<6;i++){
   cout << *(*(tmp)+i) <<"  |======>  " <<  A+i << endl;
   }
  
}