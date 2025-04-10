#include <stdio.h>

int main(void){
	int temp;
	int count[5]; //array의 원소 값이 1~5로 제한 
	int array[30] = {
		1,3,2,4,3,2,5,3,1,2,
		3,4,4,3,5,1,2,3,5,2,
		3,1,4,3,5,1,2,1,1,1
	};
	for(int i = 0; i < 5; i++){
		count[i] = 0; //count 배열의 모든 값을 0으로 초기화함 
					//count[i]는 숫자 i+1이 배열에서 등장한 횟수를 기록하기 위해 사용 
	}
	for(int i = 0; i < 30; i++){
		count[array[i]-1]++; //array[i]의 값을 count 배열에서 인덱스 array[i]-1에 1을 더함 
	}
	for(int i = 0; i < 5; i++){
		if(count[i] != 0){ //숫자 i+1이 배열에 등장한 적 있다면 해당 숫자 출력 
			for(int j = 0; j < count[i]; j++){ //count[i] 만큼 반복하면서 i+! 값을 출력 
				printf("%d", i+1);
			}
		}
	}
	return 0;
}
