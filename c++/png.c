#include <iostream>
#include <fstream>
using namespace std;

int main(int args, char **argv)
{
	const int width = 9, height = 9;;
	unsigned char image[height][width];
		string filename = "output.png";
		ofstream fout(filename);

		//画像生成
		for(int y=0; y<height; y++){
			for(int x=0;x<width; x++){
				image[y][x] = 32 * (y+x);
			}
		}

		//ファイル出力
		fout << "P2" << endl;
		fout << width << " " << height << endl;
		fout << "255" << endl;
		for(int y=0; y < height; y++){
			for(int x = 0; x < width ; x++){
				fout << (int)image[y][x] << " ";
			}
			fout << endl;
		}
		fout.flush();
		fout.close();
		
		return 0;


}
