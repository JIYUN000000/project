#include <iostream>
#include <queue>

using namespace std;

int number = 7; 
int c[7]; // 각 노드가 방문되었는지 체크 (c[i] 가 true이면 노드 i는 이미 방문한 노드) 
vector<int> a[8]; // 그래프의 인접 리스트 저장. 각 노드의 인덱스가 1부터 7이 될 수 있도록 

void bfs(int start) {
	queue<int> q;
	q.push(start); // 시작 노드에서부터 탐색 시작 
	c[start] = true; // 시작 노드를 방문했음을 표시 
	while(!q.empty()){ // 큐가 비지 않는 동안 계속 반복 
		int x = q.front(); // 큐에서 맨 앞에 있는 노드 가져옴 (이는 현재 탐색할 노드) 
		q.pop(); 
		printf("%d ", x); // 가장 먼저 방문한 노드부터 차례대로 출력 
		for(int i = 0; i < a[x].size(); i++) {
			int y = a[x][i]; // y는 x와 연결된 인접 노드 
			if(!c[y]) {
				q.push(y);
				c[y] = true;
			}
		}
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
	
	bfs(1);
	
	return 0;
	
}
