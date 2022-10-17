#!/bin/bash

for i in 5, 10, 20, 30
do  
    for j in 8, 16, 32, 64, 128
        do 
            # echo python $j, $i
            # python hello.py --id=0 --BATCH_SIZE=$j --epochs=$i
            python nn-cifar-cl-yuandou168.py --id=0 --BATCH_SIZE=$j --epochs=$i
        done
done
