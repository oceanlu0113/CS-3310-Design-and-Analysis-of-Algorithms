# -*- coding: utf-8 -*-
"""[CS3310] Project1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xdrHHqchwUpGQlh8dRpBg5tgRgCMMYPF
"""

# a. Insertion Sort

def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

# Driver code
arr = [12, 11, 13, 5, 6] 
insertionSort(arr)
print (arr)

# b. Mergesort

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

# Driver code
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print (arr)

# c. Quicksort1 (Regular Quicksort)

# This function takes last element as pivot
def partition(arr,low,high): 
    i = (low-1)
    pivot = arr[high]
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )
def quickSort1(arr,low,high): 
    if low < high:
        pi = partition(arr,low,high)
        quickSort1(arr, low, pi-1) 
        quickSort1(arr, pi+1, high) 

# Driver code 
arr = [10, 7, 8, 9, 1, 5]
quickSort1(arr,0,len(arr)-1)
print(arr)

# d. Quicksort2 (Quicksort / Insertion Sort Combo)

def partition(arr,l,h): 
    i = ( l - 1 ) 
    x = arr[h]
    for j in range(l , h): 
        if   arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return (i+1) 
def quickSort2(arr,l,h): 
    size = h - l + 1
    stack = [0] * (size) 
    top = -1
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
    while top >= 0:
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        p = partition( arr, l, h )
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
  
# Driver code
arr = [4, 3, 5, 2, 1, 3, 2, 3] 
quickSort2(arr, 0, (len(arr)-1)) 
print (arr)

# e. Quicksort3 (Randomized Quicksort)

import random 
def quickSort3(arr, start, stop): 
    if(start < stop):
        pivotindex = partitionrand(arr, start, stop)
        quickSort3(arr , start , pivotindex) 
        quickSort3(arr, pivotindex + 1, stop) 
def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, stop) 

def partition(arr,start,stop): 
    pivot = start
    i = start - 1
    j = stop + 1
    while True: 
        while True: 
            i = i + 1
            if arr[i] >= arr[pivot]: 
                break
        while True: 
            j = j - 1
            if arr[j] <= arr[pivot]: 
                break
        if i >= j: 
            return j 
        arr[i] , arr[j] = arr[j] , arr[i] 

# Driver code 
arr = [10, 7, 8, 9, 1, 5]
quickSort3(arr, 0, (len(arr)-1))
print(arr)

# time sort function

import time
import numpy as np

def makeArr(n):
  array = np.random.rand(n)
  return array

arrSize = 2
counter = 1
while (arrSize < 65537):
  print ("array size 2^", counter, "or", arrSize)
  
  # insertionSort
  arr = makeArr(arrSize)
  t0 = time.time()
  insertionSort(arr)
  t1 = time.time()
  total = t1-t0
  print ("insertionSort:", total)
  
  # mergeSort 
  arr = makeArr(arrSize)
  t0 = time.time()
  mergeSort(arr)
  t1 = time.time()
  total = t1-t0
  print ("mergeSort:", total)
  
  # quickSort1 (regular)
  arr = makeArr(arrSize)
  t0 = time.time()
  quickSort1(arr,0,len(arr)-1)
  t1 = time.time()
  total = t1-t0
  print ("quickSort1 (regular):", total)
  
  # quickSort2 (insertion)
  arr = makeArr(arrSize)
  t0 = time.time()
  quickSort2(arr,0, (len(arr)-1))
  t1 = time.time()
  total = t1-t0
  print ("quickSort2 (insertion):", total)
  
  # quickSort3 (randomized)
  arr = makeArr(arrSize)
  t0 = time.time()
  quickSort3(arr,0, (len(arr)-1))
  t1 = time.time()
  total = t1-t0
  print ("quickSort3 (randomized):", total)
  
  arrSize = arrSize * 2
  counter = counter + 1
  print()