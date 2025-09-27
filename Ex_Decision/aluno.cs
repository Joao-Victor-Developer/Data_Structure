using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace aluno
{
    internal class Program
    {
/*************  ✨ Windsurf Command ⭐  *************/
        /// <summary>
        /// Main entry point
        /// </summary>
        /// <remarks>
        /// This program asks the user for their grade and then prints out whether they need to be improved, need to take a recap, or are approved.
        /// </remarks>
        /// <param name="args">Command-line arguments</param>
/*******  881dc343-6be3-4a42-a5b0-1e3f887bce0d  *******/
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
