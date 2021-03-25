# Descroption

## 問題

i num pos: 在第 pos (pos >= 0) 個插入 num，若 pos > 現在總長度，則插入在尾端
dn num: 刪除第一個出現的 num 
dan num: 刪除所有的 num
dk k: 刪除第 k 個
p front_k: 最鄰近 head 的 front_k 個 element (由近到遠) 
mean: 將所有數字加總取平均

### insert mode

```c
i num pos
// ex: i 5 10
在第十個位置插入 5
```
* 在第 pos (pos >= 0) 個插入 num，若 pos > 現在總長度，則插入在尾端

### delete mode

#### delete number

```c
dn num
// ex: dn 5
刪除第一個出現的 5
```
* 若 num 不存在，則輸出 `delete error`

#### delete all number

```c
dan num
// ex: dan 5
刪除所有出現的 5
```
* 若 num 不存在，則輸出 `delete error`

#### delete position k

```c
dk k
// ex: dk 5
刪除第五個
```
* 若 第 k 個不存在，則輸出 `delete error`

### Output

#### print

```c
p front_k
// p 5
// print 前五的鄰近 head 的element
```
* 輸出鄰近 head 的前 front_k 個 item

### mean
```c
m
```
* 將所有數字加總取平均
* 取至小數點下第二位
