selfsort <- function(x){
        if(length(x)>1){
                min<-which.min(x)
c(x[min],selfsort(x[-min]))
}else x
}
dulieu <- c(32, 17, 49, 98, 06, 25, 53, 61)
selfsort(dulieu)


#sắp xếp chèn
insertion_sort <-function(x){
        n<-length(x)
        for(i in 2:(n)){
                temp<-x[i]
                j=i-1
        while((x[j]>temp)&& (j>=0)){
                x[j+1]  =x[j]
                j=j-1
        }
                x[j+1]=temp
                }
        return(x)
}


#bubble_sort
x<-sample(1:100,10)
example <- function(x){
        n<-length(x)
        for(j in 1:(n-1)){
                for(i in 1:(n-j)){
                        if(x[i]>x[i+1]){
                                temp<-x[i]
                                x[i]<-x[i+1]
                                x[i+1]<-temp
                        }
                }
        }
        return(x)
}


#bubble_sort2:

bubble_sort <- function(a){
        i=1
        repeat{
                no_exchange=1
                n = length(a)
                for (j in n:2){
                        if(a[j-1] > a[j]){
                                temp = a[(j-1)]
                                a[j] = temp
                                no_exchange = 0
                        }
                }
                i = i+1
                if (no_exchange || j == (n-1)) {break}
        }
        return(a)
}

#quick sort
> # Quick sort algorithm:
quickSort <- function(arr) {
mid <- sample(arr, 1)
left <- c()
right <- c()
# Move all the smaller values to the left, bigger values to the right.
lapply(arr[arr != mid], function(d) {
        if (d < mid) {
                left <<- c(left, d)
                }
        else {
                right <<- c(right, d)
                }
        })
                                
if (length(left) > 1) {
        left <- quickSort(left)
        }
                                
if (length(right) > 1) {
        right <- quickSort(right)
        }
                                
# Finally, return the sorted values.
c(left, mid, right)
}
x <-sample(1:100,10)
RES <- quickSort(x)
RES
 