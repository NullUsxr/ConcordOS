extern "C" int main(){
	*(char*)0xb8000 = 'C';
	*(char*)0xb8000 = 'C';
	*(char*)0xb8000 = 'E';
	return 0;
}
