#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    int p=1;
    string x;
    cout<<"Загадайте число от 1 до 100, а я его угадаю."<< "\n"; 
    cout<<"Введите y если готовы."<< "\n"; 
    cout<<"Введите n если не хотите играть: ";
    cin>>x;
     if(x=="y"||x=="Y")
       {
        int randomMax = 100;
        int D=0;
        while (true)
        {
            int randomNumber = rand();
            int nomer = (randomNumber % (randomMax-D))+1+D;
            cout << nomer;
            cout << "  Угадал ? y/n";
            cin>>x;
               if(x=="y"||x=="Y")
                 {
                  cout<< "Это было легко нупас ,Я угадал c " << p << " раза" <<endl;
                  break;
                 }
               else if(x=="n"||x=="N")
                 {
                  p=p+1;
                  cout<<"Больше ли загадоное число чем " << nomer << " ? y/n" <<endl;
                  cin>>x;
                     if(x=="y"||x=="Y")
                      {
                       D=nomer;
                      }
                     else if(x=="n"||x=="N")
                      {
                       randomMax=nomer;
                       continue;
                       
                       
                      }
                  }
        }
       
     }else if(x=="n"||x=="N")
       cout << "Ну ты и скучный" << endl;
       abort;
    return 0;
}
