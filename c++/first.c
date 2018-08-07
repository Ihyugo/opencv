#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

string win_src = "src";
string win_src = "dst";

int main(int args, char **argv)
{
	string file_src = "src.png";
	string file_dst = "dst.png";
	Mat img_src = imread(file_src, 1);

