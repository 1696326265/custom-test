#include<bits/stdc++.h>
#include<sys/time.h>
using namespace std;
/*
int main(){
	freopen("fuck.sh","w",stdout);
	puts("ulimit -t 2");
	puts("./while1");
	fclose(stdout);
	system("bash fuck.sh");
	cerr<<"fuckdown"<<endl;
}
*/

long long gettime(){
	timeval tv;
	gettimeofday(&tv,NULL);
	long long x = tv.tv_sec*1000000ll + tv.tv_usec;
}

int main(){
	while (1){
		system("sleep 1");
		system("ls>files");
		{
			FILE *fs=fopen("files","r");
			char s[2333], str[2333];
			while (fscanf(fs,"%s",s)!=-1){
				int l=strlen(s);
				if (l>=5&&s[l-3]=='c'&&s[l-2]=='p'&&s[l-1]=='p'&&isdigit(s[0])){
				
					s[l-4]=s[l-3]=s[l-2]=s[l-1]=s[l]=0;
					sprintf(str,"g++ %s.cpp -o %s -O2 -std=c++11",s,s); system(str);
					{
						FILE *sh=fopen("fuck.sh","w");
						fprintf(sh,"ulimit -t 11\n");
						fprintf(sh,"./%s<%s.in>%s.out\n",s,s,s);
						fclose(sh); 
					}
					long long stim=gettime();
					system("bash fuck.sh");
					long long ttim=gettime();
					{
						sprintf(str,"%s.ans",s);
						FILE *ans=fopen(str,"w");
						
						fprintf(ans,"timeusd :\n%lf\n\n",(double)(ttim-stim)/1e6);
						
						fprintf(ans,"output :\n");
						{
							sprintf(str,"%s.out",s);
							FILE *out=fopen(str,"r");
							for (int sb=1;sb<=100;++sb){
								char c;
								if (fscanf(out,"%c",&c)==-1) break;
								fprintf(ans,"%c",c);
							}
							fclose(out);
						}
						fprintf(ans,"\n");
						
						fclose(ans);
					}
					
					sprintf(str,"rm %s.cpp",s);
					system(str);
					
					break;
				}
			}
			fclose(fs);
		}
	}
}






