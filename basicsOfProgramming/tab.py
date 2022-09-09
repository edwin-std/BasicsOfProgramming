import dash
import dash_bootstrap_components as dbc
import dash_gif_component as gif
from dash import html
from dash import dash_table as dt
from dash import dcc
from dash.dependencies import Input, Output, State

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Markdown('''
            ## Bubble sort in Python
            
            ```python
            def bubbleSort(array):
            #Зацикливаем,что бы получить доступ к каждому жлементу массива
            for i in range(len(array)):

            #Цикл для сравнения элементов массива
            for j in range(0, len(array) - i - 1):

            #Сравниваем первый элемент масссива с следующим
            #(поменять > на < для сортировки в порядке убывания)
            if array[j] > array[j + 1]:

            #Меняем местами элементы, если выполняется условие 
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

            data = ([-2, 45, 0, 11, -9])
            
            bubbleSort(data)
            
            print('Sorted Array in Ascending Order:')
            print(data)
            ```''')
        ]
    ),
    className="mt-3", style={}
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Markdown('''
            ## Bubble sort in Java
            
            ```java
            import java.util.Arrays;
            class Main {
              //perform the bubble sort
              static void bubbleSort(int array[]) {
                int size = array.length;
                
                 //loop to access each array element
                for (int i = 0; i < size - 1; i++)
                
                   //loop to compare array elements
                  for (int j = 0; j < size - i - 1; j++)
            
                    // compare two adjacent elements
                    // change > to < to sort in descending order
                    if (array[j] > array[j + 1]) {
            
                      // swapping occurs if elements
                      // are not in the intended order
                      int temp = array[j];
                      array[j] = array[j + 1];
                      array[j + 1] = temp;
                    }
              }
              public static void main(String args[]) {
                  
                int[] data = { -2, 45, 0, 11, -9 };
                
                // call method using class name
                Main.bubbleSort(data);
                
                System.out.println("Sorted Array in Ascending Order:");
                System.out.println(Arrays.toString(data));
              }
            }
            ```''')
        ]
    ),
    className="mt-3", style={}
)
tab3_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
        ## Bubble sort in C++
        
        ```cpp
        #include <iostream>
        using namespace std;
        
        // perform bubble sort
        void bubbleSort(int array[], int size) {
        
          // loop to access each array element
          for (int step = 0; step < size; ++step) {
              
            // loop to compare array elements
            for (int i = 0; i < size - step; ++i) {
        
              // compare two adjacent elements
              // change > to < to sort in descending order
              if (array[i] > array[i + 1]) {
        
                // swapping elements if elements
                // are not in the intended order
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
              }
            }
          }
        }
        // print array
        void printArray(int array[], int size) {
          for (int i = 0; i < size; ++i) {
            cout << " " << array[i];
          }
          cout << "/n";
        }
        int main() {
          int data[] = {-2, 45, 0, 11, -9};
          
          // find array's length
          int size = sizeof(data) / sizeof(data[0]);
          
          bubbleSort(data, size);
          
          cout << "Sorted Array in Ascending Order:/n";  
          printArray(data, size);
        }
        ```''')
    ])
)
tab4_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
        ## Insertion sort in Python
        
        ```python
        def insertionSort(array):

        for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left
        # of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

        data = [9, 5, 1, 4, 3]
        insertionSort(data)
        print('Sorted Array in Ascending Order:')
        print(data)
        
        ```''')
    ])
)
tab5_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
        ## Insertion sort in Java
        ```java
        import java.util.Arrays;
        
        class InsertionSort {
        
          void insertionSort(int array[]) {
            int size = array.length;
        
            for (int step = 1; step < size; step++) {
              int key = array[step];
              int j = step - 1;
        
              // Compare key with each element on the left 
              // of it until an element smaller than it is found.
              // For descending order, change key<array[j] to key>array[j].
              while (j >= 0 && key < array[j]) {
                array[j + 1] = array[j];
                --j;
              }
        
              // Place key at after the element just smaller than it.
              array[j + 1] = key;
            }
          }
        
          // Driver code
          public static void main(String args[]) {
            int[] data = { 9, 5, 1, 4, 3 };
            InsertionSort is = new InsertionSort();
            is.insertionSort(data);
            System.out.println("Sorted Array in Ascending Order: ");
            System.out.println(Arrays.toString(data));
          }
        }
        
        ```''')
    ])
)
tab6_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
        
        ```cpp
        #include <iostream>
        using namespace std;
        
        // Function to print an array
        void printArray(int array[], int size) {
          for (int i = 0; i < size; i++) {
            cout << array[i] << " ";
          }
          cout << endl;
        }
        
        void insertionSort(int array[], int size) {
          for (int step = 1; step < size; step++) {
            int key = array[step];
            int j = step - 1;
        
            // Compare key with each element on the left 
            //of it until an element smaller than it is found.
            // For descending order, change key<array[j] to key>array[j].
            while (key < array[j] && j >= 0) {
              array[j + 1] = array[j];
              --j;
            }
            array[j + 1] = key;
          }
        }
        
        // Driver code
        int main() {
          int data[] = {9, 5, 1, 4, 3};
          int size = sizeof(data) / sizeof(data[0]);
          insertionSort(data, size);
          cout << "Sorted array in ascending order:/n";
          printArray(data, size);
        }
        
        ```''')
    ])
)
tab7_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
        ## Merge sort in Python
        
        ```python
        def mergeSort(array):
        if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

        # Print the array
        def printList(array):
            for i in range(len(array)):
                print(array[i], end=" ")
            print()
    
        # Driver program
        if __name__ == '__main__':
        array = [6, 5, 12, 10, 9, 1]
    
        mergeSort(array)
    
        print("Sorted array is: ")
        printList(array)
        
        ```''')
    ])
)

tab8_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
    ## Merge sort in Java
        
    ```java 
     class MergeSort {
              void merge(int arr[], int p, int q, int r) {
                
                int n1 = q - p + 1;
                int n2 = r - q;
            
                int L[] = new int[n1];
                int M[] = new int[n2];
            
                for (int i = 0; i < n1; i++)
                  L[i] = arr[p + i];
                for (int j = 0; j < n2; j++)
                  M[j] = arr[q + 1 + j];
            
                int i, j, k;
                i = 0;
                j = 0;
                k = p;
            
                while (i < n1 && j < n2) {
                  if (L[i] <= M[j]) {
                    arr[k] = L[i];
                    i++;
                  } else {
                    arr[k] = M[j];
                    j++;
                  }
                  k++;
                }
                
                while (i < n1) {
                  arr[k] = L[i];
                  i++;
                  k++;
                }
            
                while (j < n2) {
                  arr[k] = M[j];
                  j++;
                  k++;
                }
              }
            
              void mergeSort(int arr[], int l, int r) {
                if (l < r) {
                  int m = (l + r) / 2;
            
                  mergeSort(arr, l, m);
                  mergeSort(arr, m + 1, r);
            
                  merge(arr, l, m, r);
                }
              }
            
              static void printArray(int arr[]) {
                int n = arr.length;
                for (int i = 0; i < n; ++i)
                  System.out.print(arr[i] + " ");
                System.out.println();
              }
            
              public static void main(String args[]) {
                int arr[] = { 6, 5, 12, 10, 9, 1 };
            
                MergeSort ob = new MergeSort();
                ob.mergeSort(arr, 0, arr.length - 1);
            
                System.out.println("Sorted array:");
                printArray(arr);
              }
            }''')
    ])
)

tab9_content = dbc.Card(
    dbc.CardBody([
        dcc.Markdown('''
        ## Merge sort in C++
        
        ```cpp
        #include <iostream>
        using namespace std;
        
        // Merge two subarrays L and M into arr
        void merge(int arr[], int p, int q, int r) {
          
          // Create L ← A[p..q] and M ← A[q+1..r]
          int n1 = q - p + 1;
          int n2 = r - q;
        
          int L[n1], M[n2];
        
          for (int i = 0; i < n1; i++)
            L[i] = arr[p + i];
          for (int j = 0; j < n2; j++)
            M[j] = arr[q + 1 + j];
        
          // Maintain current index of sub-arrays and main array
          int i, j, k;
          i = 0;
          j = 0;
          k = p;
        
          // Until we reach either end of either L or M, pick larger among
          // elements L and M and place them in the correct position at A[p..r]
          while (i < n1 && j < n2) {
            if (L[i] <= M[j]) {
              arr[k] = L[i];
              i++;
            } else {
              arr[k] = M[j];
              j++;
            }
            k++;
          }
        
          // When we run out of elements in either L or M,
          // pick up the remaining elements and put in A[p..r]
          while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
          }
        
          while (j < n2) {
            arr[k] = M[j];
            j++;
            k++;
          }
        }
   
        // Divide the array into two subarrays, sort them and merge them
        void mergeSort(int arr[], int l, int r) {
          if (l < r) {
            // m is the point where the array is divided into two subarrays
            int m = l + (r - l) / 2;
        
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
        
            // Merge the sorted subarrays
            merge(arr, l, m, r);
          }
        }
        
        // Print the array
        void printArray(int arr[], int size) {
          for (int i = 0; i < size; i++)
            cout << arr[i] << " ";
          cout << endl;
        }
        
        // Driver program
        int main() {
          int arr[] = {6, 5, 12, 10, 9, 1};
          int size = sizeof(arr) / sizeof(arr[0]);
        
          mergeSort(arr, 0, size - 1);
        
          cout << "Sorted array: /n";
          printArray(arr, size);
          return 0;
        }
        ```''')
    ])
)
