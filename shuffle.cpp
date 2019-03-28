#include <iostream>
#define SIZE 1000
#include <cstdlib>
#include <ctime>


using namespace std;
void sortArr(int arr[]);
void swap(int arr[],int index1,int index2);
void fillArray(int arr[]);
void nullArray(int arr[]);
void shuffleArray(int arr[])

{
int main()
{
    srand(time(null));
    array1[SIZE];
    fillArray(array1);
    for (int i = 0 ; i < SIZE; i++)
    {
        cout << array1[i] << endl;
    }
    }
    return 0;
}
void fillArray(int arr[])
{
   for(int i = 0; i < SIZE; i++){
        arr[i] = i+1;
    }

}
void shuffleArray(int arr[])
{
    for (int i = 0; i < SIZE; i++)
        {
        int r = rand() % SIZE+1;
        swap(arr[i], r, i);
        }
}
}
void nullArray(int arr[])
{
    for(int i = 0; i < SIZE; i++){
        arr[i] = 0;
    }

}
void sortArr(int arr[])
{
    int min;
    int posOfMin; 
    for(int outter = 0; outter < SIZE; outter++)
    {
        min = arr[outter];
        posOfMin = outter;
 
        for(int inner = outter + 1; inner < SIZE ; inner++)
        {
            if(arr[inner] < min)
            {
                min = arr[inner];
                posOfMin = inner;
            }
        }
        swap(arr, outter, posOfMin);
    }
}

 
    for(int outter = 0; outter < SIZE; outter++)
    {
        min = arr[outter];
        posOfMin = outter;
 
        for(int inner = outter + 1; inner < SIZE ; inner++)
        {
            if(arr[inner] < min)
            {
                min = arr[inner];
                posOfMin = inner;
            }
        }
        swap(arr, outter, posOfMin);
    }
}

 void swap(int arr[],int index1,int index2)
{
    int temp;
    temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
 
}
