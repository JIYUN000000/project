#include <iostream>
#include <vector> // vector라는 동적 배열을 사용하기 위함 
#include <algorithm>

// 두 개의 변수를 기준으로 정렬하기 
using namespace std;

bool compare(pair<string, pair<int, int> > a,
			 pair<string, pair<int, int> > b) {
	if(a.second.first == b.second.first){
		return a.second.second > b.second.second;
	} else {
		return a.second.first > b.second.first;
	}
}


int main(void){
	vector<pair<string, pair<int, int> > > v; // int와 string을 하나의 묶음으로 저장하는 pair 자료구조 
	v.push_back(pair<string, pair<int, int> >("김지윤", pair<int, int>(90, 20010509))); // push_back: 리스트의 마지막 부분에 삽입 
	v.push_back(pair<string, pair<int, int> >("김채훈", pair<int, int>(97, 20020306)));
	v.push_back(pair<string, pair<int, int> >("장유나", pair<int, int>(95, 20030507))); 
	v.push_back(pair<string, pair<int, int> >("박성경", pair<int, int>(90, 20040506)));
	v.push_back(pair<string, pair<int, int> >("김남희", pair<int, int>(88, 20050708)));
		
	sort(v.begin(), v.end(), compare); // 벡터의 첫 번째 값부터 마지막 값까지 정렬 
	for(int i = 0; i < v.size(); i++){
		cout << v[i].first << ' '; // first: 이름 정보 
	}
	return 0;
	 
}
