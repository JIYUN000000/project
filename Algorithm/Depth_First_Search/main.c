#include <iostream>
#include <vector>

using namespace std;

int number = 7; // 그래프 노드 개수 
int c[7]; // 각 노드가 방문되었는지 체크 (c[i]가 true이면 노드 i는 이미 방문한 노드) 
vector<int> a[8]; // 그래프의 인접 리스트 저장 (각 노드의 인덱스가 1부터 7까지 되도록 크기 8로 설정) 

void dfs(int x){
	if(c[x]) return; // 이미 방문한 노드라면 더 이상 탐색하지 않음 
	c[x] = true; // 현재 노드를 방문 처리 
	cout << x << ' '; // 탐색 순서대로 출력 
	for(int i=0; i < a[x].size(); i++) {
		int y = a[x][i]; // x와 연결된 i번째 노드를 y에 저장 
		dfs(y); // 연결된 노드 y에 대해 DFS 호출 
	}
}

int main(void) {
	a[1].push_back(2);
	a[2].push_back(1);
	
	a[1].push_back(3);
	a[3].push_back(1);
	
	a[2].push_back(3);
	a[3].push_back(2);
	
	a[2].push_back(4);
	a[4].push_back(2);
	
	a[2].push_back(5);
	a[5].push_back(2);
	
	a[4].push_back(5);
	a[5].push_back(4);
	
	a[3].push_back(6);
	a[6].push_back(3);
	
	a[3].push_back(7);
	a[7].push_back(3);
	
	a[6].push_back(7);
	a[7].push_back(6);
	
	dfs(1);
	
	return 0;
	
}
