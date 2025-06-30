#include <iostream>
#include <vector> // vector라는 동적 배열을 사용하기 위함 
#include <algorithm>

using namespace std;

int main(void){
	vector<pair<int, string> > v; // int와 string을 하나의 묶음으로 저장하는 pair 자료구조 
	v.push_back(pair<int, string>(90, "김지윤")); // push_back: 리스트의 마지막 부분에 삽입 
	v.push_back(pair<int, string>(82, "김채훈"));
	v.push_back(pair<int, string>(98, "장유나"));
	v.push_back(pair<int, string>(79, "김남희"));
	v.push_back(pair<int, string>(85, "박성경"));
	
	sort(v.begin(), v.end()); // 벡터의 첫 번째 값부터 마지막 값까지 정렬 
	for(int i = 0; i < v.size(); i++){
		cout << v[i].second << ' '; // second: 이름 정보 
	}
	return 0;
	 
}
