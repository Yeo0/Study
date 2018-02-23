#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>

enum {
	BLACK, BLUE, GREEN, SKY_BLUE, RED, PURPLE, YELLOW, WHITE, GRAY, BRIGHT_GRAY, BRIGHT_GREEN, BRIGHT_SKY_BLUE, BRIGHT_RED, BRIGHT_PURPLE, BRIGHT_YELLOW, DEEP_WHITE
};
typedef struct set {
	int ** frame;
	int * mine;
	int ** check;
	int ** flag;
	int frameSize;
	int mineSize; //°³¼ö
}SET;

int getRandom(int start, int range);
void printFrame(int** frame, int frameSize, int ** check, int ** flag);
void setMine(SET set);
void setNumber(int** frame, int frameSize);
void checkBox(int ** check, int x, int y, int frameSize, int ** frame);
int checkHeartCount(int x, int y, int frameSize, int** flag);

void setColor(int color) {
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

void gotoxy(int x, int y) {
	COORD pos = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void main(){
	SET mineSet;
	int i, j;
	int random;
	char key;
	int curX=0, curY=0;
	int countChecker;
	gotoxy(50, 25);
	printf("type frame size : ");
	scanf("%d", &mineSet.frameSize);
	mineSet.mineSize = mineSet.frameSize * 4 - 10;
	mineSet.frame = (int**)malloc(sizeof(int*)*mineSet.frameSize);
	mineSet.check = (int**)malloc(sizeof(int*)*mineSet.frameSize);
	mineSet.flag = (int**)malloc(sizeof(int*)*mineSet.frameSize);
	for (i = 0; i < mineSet.frameSize; i++){
		mineSet.frame[i] = (int*)calloc(sizeof(int), mineSet.frameSize);
		mineSet.check[i] = (int*)calloc(sizeof(int), mineSet.frameSize);
		mineSet.flag[i] = (int*)calloc(sizeof(int), mineSet.frameSize);
	}
	mineSet.mine = (int*)malloc(sizeof(int)*mineSet.mineSize);

	srand(time(NULL));
	
	for (i = 0; i < mineSet.mineSize; i++){
		random = getRandom(0, mineSet.frameSize*mineSet.frameSize);
		mineSet.mine[i] = random;
		for (j = 0; j < i; j++){
			if (mineSet.mine[i] == mineSet.mine[j]) i--;
		}
	}
	/*
	printf("Áö·Ú ÀÎµ¦½º : ");
	for (i = 0; i < mineSet.mineSize; i++){
		printf("%d ", mineSet.mine[i]);
	}
	printf("\n");
	*/
	setMine(mineSet);
	//printFrame(mineSet.frame, mineSet.frameSize);
	setNumber(mineSet.frame, mineSet.frameSize);
	printFrame(mineSet.frame, mineSet.frameSize, mineSet.check, mineSet.flag);
	printf("\n\n\n\n\n\n");
	for (i = 0; i < mineSet.frameSize; i++){
		for (j = 0; j < mineSet.frameSize; j++){
			printf("%2d", mineSet.frame[i][j]);
		}
		printf("\n");
	}
	gotoxy(curX, curY);
	key = ' ';
	while (1) {
		key = getch();
		if (key == 72) {
			if (curY > 0) {
				curY--;
			}
		}
		else if (key == 75) {
			if (curX > 0) {
				curX -= 2;
			}
		}
		else if (key == 80) {
			if (curY < mineSet.frameSize - 1) {
				curY++;
			}
		}
		else if (key == 77) {
			if (curX < mineSet.frameSize * 2 - 2) {
				curX += 2;
			}
		}
		else if (key == 'q') {
			exit(0);
		}
		else if (key == 13) {
			if (mineSet.check[curY][curX / 2] == 1) {
				countChecker = checkHeartCount(curY, curX / 2, mineSet.frameSize, mineSet.flag, mineSet.frame);
				if (countChecker == -1) {
					for (i = 0; i < mineSet.mineSize; i++) {
						gotoxy(2*(mineSet.mine[i] % mineSet.frameSize), mineSet.mine[i] / mineSet.frameSize);
						printf("-1");
					}
					gotoxy(10, 10);
					setColor(BRIGHT_RED);
					printf("¡Ú¡Ù¡Ú¡Ù¡Ú¡Ù Boooooom ¡Ú¡Ù¡Ú¡Ù¡Ú¡Ù\n\n");
					exit(0);
				}
				else if (mineSet.frame[curY][curX / 2] == countChecker) {
					checkBox(mineSet.check, curY, curX / 2, mineSet.frameSize, mineSet.frame);
				}
			}
			else {
				mineSet.check[curY][curX / 2] = 1;
				if (mineSet.frame[curY][curX / 2] == -1) {
					gotoxy(10, 10);
					setColor(BRIGHT_RED);
					printf("¡Ú¡Ù¡Ú¡Ù¡Ú¡Ù Boooooom ¡Ú¡Ù¡Ú¡Ù¡Ú¡Ù\n\n");
					exit(0);
				}
				else if (mineSet.frame[curY][curX / 2] == 0) {
					checkBox(mineSet.check, curY, curX / 2, mineSet.frameSize, mineSet.frame);
				}
			}
			printFrame(mineSet.frame, mineSet.frameSize, mineSet.check, mineSet.flag);
		}
		else if (key == 'f') {
			if (mineSet.flag[curY][curX / 2] == 1) {
				mineSet.flag[curY][curX / 2] = 0;
			}
			else {
				mineSet.flag[curY][curX / 2] = 1;
			}
			printFrame(mineSet.frame, mineSet.frameSize, mineSet.check, mineSet.flag);
		}
		gotoxy(curX, curY);

	}
}

int getRandom(int start, int range){
	int randomNumber = rand() % range + start;
	return randomNumber;
}

void printFrame(int** frame, int frameSize, int ** check, int ** flag){

	int i, j;

	system("cls");
	for (i = 0; i < frameSize; i++){
		for (j = 0; j < frameSize; j++){
			if (check[i][j] == 1) {
				printf("%2d", frame[i][j]);
			}
			else if (flag[i][j] == 1) {
				setColor(BRIGHT_SKY_BLUE);
				printf("¢¾");
				setColor(DEEP_WHITE);
			}
			else {
				printf("¡á");
			}
		}
		printf("\n");
	}
}

void setMine(SET set){
	int i;
	for (i = 0; i < set.mineSize; i++){
		set.frame[set.mine[i] / set.frameSize][set.mine[i] % set.frameSize] = -1;
	}
}

void setNumber(int** frame, int frameSize){
	int i, j,m,n;
	for (i = 0; i < frameSize; i++){
		for (j = 0; j < frameSize; j++){
			if (frame[i][j] != -1){
				for (m = i - 1; m <= i + 1; m++){
					for (n = j - 1; n <= j + 1; n++){
						if (m >= 0 && m < frameSize && n >= 0 && n < frameSize){
		
							if (frame[m][n] == -1){
								frame[i][j]++;
							}

						}
					}
				}
			}
		}
	}

}

void checkBox(int ** check, int x, int y, int frameSize, int **frame) {
	int i, j;
	for (i = x - 1; i <= x + 1; i++) {
		for (j = y - 1; j <= y + 1; j++) {
			if (i >= 0 && i < frameSize && j >= 0 && j < frameSize) {
				if (check[i][j] == 0 && frame[i][j] != -1) {
					check[i][j] = 1;
					if (frame[i][j] == 0) {
						checkBox(check, i, j, frameSize, frame);
					}
				}
			}
		}
		
	}
}

int checkHeartCount(int x, int y, int frameSize, int** flag, int** frame) {
	int i, j;
	int count = 0;
	for (i = x - 1; i <= x + 1; i++){
		for (j = y - 1; j <= y + 1; j++){
			if (i >= 0 && i < frameSize && j >= 0 && j < frameSize){
				if (flag[i][j] == 1) {
					if (frame[i][j] != -1) {
						return -1;
					}
					else {
						count++;
					}
				}
			}

		}
	}
	return count;
}



