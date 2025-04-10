#include <iostream>
#include <algorithm>

using namespace std;

string a[20000];
int n;

bool compare(string a, string b){
	// 길이가 짧은 순서 우선
	if(a.length() < b.length()){
		return 1;
	} else if(a.length() > b.length()){
		return 0;
	} 
	// 길이가 같은 경우 
	else {
		return a < b; // 사전순으로 정렬 
	}
}

int main(void){
	cin >> n; // 배열 크기 n 입력받음 
	for(int i=0; i < n; i++){
		cin >> a[i]; // 배열 a[]의 각 원소에 입력된 값을 하나씩 저장 
	}
	sort(a, a+n, compare); // 배열의 시작 주소(a)부터 끝 주소(a+n)까지 compare 함수를 기준으로 정렬 
	for(int i=0; i<n; i++){
		if(i>0 && a[i] == a[i-1]){ // 중복된 원소는 출력하지 않도록 
			continue;
		} else {
			cout << a[i] << '\n'; // 중복되지 않은 값만 출력 
		}
		
	}
} 
