#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long comparisons = 0;

// ---------------- Utility ----------------
void resetComparisons() {
    comparisons = 0;
}

// ---------------- Selection Sort ----------------
void selectionSort(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        int min = i;
        for(int j = i+1; j < n; j++) {
            comparisons++;
            if(arr[j] < arr[min])
                min = j;
        }
        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

// ---------------- Bubble Sort ----------------
void bubbleSort(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            comparisons++;
            if(arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// ---------------- Insertion Sort ----------------
void insertionSort(int arr[], int n) {
    for(int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && (++comparisons && arr[j] > key)) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

// ---------------- Merge Sort ----------------
void merge(int arr[], int l, int m, int r) {
    int n1 = m-l+1, n2 = r-m;
    int L[n1], R[n2];

    for(int i=0;i<n1;i++) L[i]=arr[l+i];
    for(int i=0;i<n2;i++) R[i]=arr[m+1+i];

    int i=0,j=0,k=l;

    while(i<n1 && j<n2) {
        comparisons++;
        if(L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    while(i<n1) arr[k++] = L[i++];
    while(j<n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if(l<r) {
        int m = (l+r)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}

// ---------------- Heap Sort ----------------
void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2*i+1, r = 2*i+2;

    if(l<n){ comparisons++; if(arr[l]>arr[largest]) largest=l; }
    if(r<n){ comparisons++; if(arr[r]>arr[largest]) largest=r; }

    if(largest!=i) {
        int temp = arr[i];
        arr[i]=arr[largest];
        arr[largest]=temp;
        heapify(arr,n,largest);
    }
}

void heapSort(int arr[], int n) {
    for(int i=n/2-1;i>=0;i--)
        heapify(arr,n,i);

    for(int i=n-1;i>0;i--) {
        int temp=arr[0];
        arr[0]=arr[i];
        arr[i]=temp;
        heapify(arr,i,0);
    }
}

// ---------------- Radix Sort ----------------
void countingSort(int arr[], int n, int exp) {
    int output[n], count[10]={0};

    for(int i=0;i<n;i++)
        count[(arr[i]/exp)%10]++;

    for(int i=1;i<10;i++)
        count[i]+=count[i-1];

    for(int i=n-1;i>=0;i--) {
        output[count[(arr[i]/exp)%10]-1]=arr[i];
        count[(arr[i]/exp)%10]--;
    }

    for(int i=0;i<n;i++)
        arr[i]=output[i];
}

void radixSort(int arr[], int n) {
    int max = arr[0];
    for(int i=1;i<n;i++)
        if(arr[i]>max) max=arr[i];

    for(int exp=1;max/exp>0;exp*=10)
        countingSort(arr,n,exp);
}

// ---------------- QuickSort ----------------
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low-1;

    for(int j=low;j<high;j++) {
        comparisons++;
        if(arr[j] < pivot) {
            i++;
            int temp=arr[i]; arr[i]=arr[j]; arr[j]=temp;
        }
    }
    int temp=arr[i+1]; arr[i+1]=arr[high]; arr[high]=temp;
    return i+1;
}

// First pivot
void quickFirst(int arr[], int low, int high) {
    if(low<high) {
        int temp=arr[low]; arr[low]=arr[high]; arr[high]=temp;
        int pi=partition(arr,low,high);
        quickFirst(arr,low,pi-1);
        quickFirst(arr,pi+1,high);
    }
}

// Random pivot
void quickRandom(int arr[], int low, int high) {
    if(low<high) {
        int r = low + rand()%(high-low+1);
        int temp=arr[r]; arr[r]=arr[high]; arr[high]=temp;
        int pi=partition(arr,low,high);
        quickRandom(arr,low,pi-1);
        quickRandom(arr,pi+1,high);
    }
}

// Median pivot
int median(int arr[], int low, int high) {
    int mid=(low+high)/2;
    if(arr[low]>arr[mid]) {int t=arr[low];arr[low]=arr[mid];arr[mid]=t;}
    if(arr[low]>arr[high]){int t=arr[low];arr[low]=arr[high];arr[high]=t;}
    if(arr[mid]>arr[high]){int t=arr[mid];arr[mid]=arr[high];arr[high]=t;}
    return mid;
}

void quickMedian(int arr[], int low, int high) {
    if(low<high) {
        int m = median(arr,low,high);
        int temp=arr[m]; arr[m]=arr[high]; arr[high]=temp;
        int pi=partition(arr,low,high);
        quickMedian(arr,low,pi-1);
        quickMedian(arr,pi+1,high);
    }
}



void copyArray(int src[], int dest[], int n) {
    for(int i=0;i<n;i++) dest[i]=src[i];
}

void generateRandom(int arr[], int n) {
    for(int i=0;i<n;i++) arr[i] = rand()%10000;
}

void generateSorted(int arr[], int n) {
    for(int i=0;i<n;i++) arr[i] = i;
}

void generateReverse(int arr[], int n) {
    for(int i=0;i<n;i++) arr[i] = n-i;
}

int main() {
    srand(time(NULL));

    int sizes[] = {100, 500, 1000};
    int numSizes = 3;

    FILE *fp = fopen("results.csv", "w");

    fprintf(fp, "Algorithm,InputType,N,Time,Comparisons\n");

    for(int s=0;s<numSizes;s++) {
        int n = sizes[s];

        int arr[n], temp[n];

        // 3 types of input
        for(int type=0; type<3; type++) {

            if(type==0) generateRandom(arr,n);
            else if(type==1) generateSorted(arr,n);
            else generateReverse(arr,n);

            char *typeName = (type==0)?"Random":(type==1)?"Sorted":"Reverse";

            // ---------- Selection Sort ----------
            copyArray(arr,temp,n);
            resetComparisons();
            clock_t start = clock();
            selectionSort(temp,n);
            clock_t end = clock();

            fprintf(fp,"Selection,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Bubble ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            bubbleSort(temp,n);
            end = clock();

            fprintf(fp,"Bubble,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Insertion ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            insertionSort(temp,n);
            end = clock();

            fprintf(fp,"Insertion,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Merge ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            mergeSort(temp,0,n-1);
            end = clock();

            fprintf(fp,"Merge,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Heap ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            heapSort(temp,n);
            end = clock();

            fprintf(fp,"Heap,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Radix ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            radixSort(temp,n);
            end = clock();

            fprintf(fp,"Radix,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Quick First ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            quickFirst(temp,0,n-1);
            end = clock();

            fprintf(fp,"QuickFirst,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Quick Random ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            quickRandom(temp,0,n-1);
            end = clock();

            fprintf(fp,"QuickRandom,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);

            // ---------- Quick Median ----------
            copyArray(arr,temp,n);
            resetComparisons();
            start = clock();
            quickMedian(temp,0,n-1);
            end = clock();

            fprintf(fp,"QuickMedian,%s,%d,%lf,%lld\n",
                typeName,n,
                (double)(end-start)/CLOCKS_PER_SEC,
                comparisons);
        }
    }

    fclose(fp);
    printf("Results saved to results.csv\n");

    return 0;
}