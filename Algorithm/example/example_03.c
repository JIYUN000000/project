#include <iostream>

using namespace std;

int n;
int a[10001]; // 배열의 모든 인덱스값은 0으로 초기화 

int main(void){
	scanf("%d", &n);
	for(int i=0; i < n; i++){
		int x;
		scanf("%d", &x);
		a[x]++;
	}
	for(int i = 0; i < 10001; i++){
		while(a[i] != 0){
			printf("%d\n", i);
			a[i]--; // 중복된 값들을 반복해서 출력 
		}
	}
}
