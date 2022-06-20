using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NetApp
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Comenzando el programa de .NET");

            while (true)
            {

                // string movimiento = Console.ReadLine(); //0, -1, 1
                string entrada = Console.ReadLine();

                string[] datos = entrada.Split(',');
                string movimiento = datos[0];
                string brincar = datos[1];
                string acelerar = datos[2];

                // Logica del movimiento

                if (movimiento.Equals("0"))
                {
                    // No se mueve
                    WindowsCrap.Release(WindowsCrap.ScanCodeShort.KEY_A);
                    WindowsCrap.Release(WindowsCrap.ScanCodeShort.KEY_D);
                }
                else if (movimiento.Equals("-1"))
                {
                    // Se mueve a la izquierda
                    WindowsCrap.Press(WindowsCrap.ScanCodeShort.KEY_A);
                    WindowsCrap.Release(WindowsCrap.ScanCodeShort.KEY_D);
                }
                else if (movimiento == "1")
                {
                    //Se mueve a la derecha
                    WindowsCrap.Press(WindowsCrap.ScanCodeShort.KEY_D);
                    WindowsCrap.Release(WindowsCrap.ScanCodeShort.KEY_A);
                }

                // Logica del salto

                if (brincar.Equals("1"))
                {
                    // Salta
                    WindowsCrap.Press(WindowsCrap.ScanCodeShort.KEY_J);
                }
                else
                {
                    WindowsCrap.Release(WindowsCrap.ScanCodeShort.KEY_J);
                }

                // Aceleracion

                if (acelerar.Equals("1"))
                {
                    // Aceleramos
                    WindowsCrap.Press(WindowsCrap.ScanCodeShort.SPACE);
                }
                else
                {
                    // Dejamos de acelerar
                    WindowsCrap.Release(WindowsCrap.ScanCodeShort.SPACE);
                }

            }

        }
    }
}
