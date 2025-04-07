#include <iostream>
#include <algorithm>

using namespace std;

class Student {
	public:
		string name;
		int score;
		Student(string name, int score){
			this->name = name;
			this->score = score;
		}
		// 정렬 기준은 '점수가 작은 순서'
		bool operator < (Student &student){ // 참조자(&)로 객체를 직접 참조, Student 객체끼리 비교 
			return this->score < student.score; // 두 학생 객체의 점수 비교, 점수가 작은 순서대로 정렬 
		}
};

int main(void){
	Student students[] = {
		Student("김지윤", 90),
		Student("장유나", 93),
		Student("김남희", 97),
		Student("김채훈", 91),
		Student("박성경", 92)
	};
	sort(students, students + 5); // 배열 정렬 함수 sort로 두 학생 객체를 점수를 기준으로 오름차순으로 정렬 
	for(int i = 0; i < 5; i++){
		cout << students[i].name << ' ';
	}
}

