#include<stdio.h>
#include<string.h>



int trim(char string[])
{
  int i,j;
  for(i=0;i<strlen(string);i++)
    if(string[i]==' '||string[i]=='t')
      {
	for(j=i+1;j<strlen(string);j++)
	  string[j-1]=string[j];
	string[j-1]='';
	i--;
      }
}

int substring(char string[],char substring[])
{
  int j,k;
  for(j=0;j<strlen(substring);j++)
    {
      for(k=0;k<strlen(string);k++)
	if(substring[j]==string[k]) break;
      if(k==strlen(string)) return 0;
    }
  return 1;
}


int main()
{
  char attr[20],fds[10][20],key[20],left[20],right[20];
  int nooffds,noofattr,bcnf=1,tnf=1,found=0,i,j,k;


  printf("Enter the number of attributes n");
  scanf("%d",&noofattr);

  for(i=0;i<noofattr;i++)
    {attr[i]='A'+i;printf("%c",attr[i]);if(i!=noofattr-1) printf(",");}
  printf("n");

  printf("Enter the keyn");
  scanf("%s",key);
  trim(key);strdup(key);
  printf("Enter the number of fdsn");
  scanf("%d",&nooffds);

  for(i=0;i<nooffds;i++) 
    {
      scanf("%s",fds[i]);
      trim(fds[i]);
      strdup(fds[i]);
    }

  for(i=0;i<nooffds;i++)
    {
      for(k=0,found=0,j=0;j<strlen(fds[i]);j++)
	{
	  if(fds[i][j]=='-') {
	    left[k]='';
	    k=0;j++;
	    found=1;
	  }

	  else if(found==0) left[k++]=fds[i][j];

	  else right[k++]=fds[i][j];

	}
      right[k]='';
      if(substring(left,key)==0)
	{
	  bcnf=0;
	  printf("%s Violates BCNF Conditionsn",fds[i]);

	  if(substring(key,right)==0)
	    {
	      tnf=0;
	      printf("and Violates 3 NF Conditionsn");
	      break;
	    }

	}
    }

  if(tnf==0)printf("Neither BCNF nor 3NF");

  else if(bcnf==0)printf("In 3NF but not in BCNF");

  else printf("is in both BCNF and 3NF");

}
