using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace aluno
{
    internal class Program
    {
        static void Main(string[] args)
        {

            double nota;

            Console.WriteLine("Digite sua nota: ");
            nota = Convert.ToDouble(Console.ReadLine());

            if (nota <= 5) {
                Console.WriteLine("Reproved");
            }
            else if (nota <=6) {
                Console.WriteLine("Recuparation");


            }
            else if(nota >6)
            {
                Console.WriteLine("Aprovved");
            }








            Console.ReadKey();
        }
    }
}
