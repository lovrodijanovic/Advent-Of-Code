using System;
using System.Collections.Generic;

namespace Advent_of_code_2020_day1
{
    class Program
    {
        static void Main(string[] args)
        {
            firstPuzzle();
        }
        static void firstPuzzle()
        {
            List<int> values = new List<int>();

            foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\2020\Advent-of-code-2020-day1\input.txt"))
            {
                values.Add(int.Parse(line));
            }

            int[] valuesArray = values.ToArray();

            for (int i = 0; i < valuesArray.Length; i++)
            {
                for (int j = 0; j < valuesArray.Length; j++)
                {
                    if (valuesArray[i] + valuesArray[j] == 2020)
                    {
                        Console.WriteLine(valuesArray[i] * valuesArray[j]);
                    }
                }
            }
        }
        static void secondPuzzle()
        {
            List<int> values = new List<int>();

            foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\2020\Advent-of-code-2020-day1\input.txt"))
            {
                values.Add(int.Parse(line));
            }

            int[] valuesArray = values.ToArray();

            for (int i = 0; i < valuesArray.Length; i++)
            {
                for (int j = 0; j < valuesArray.Length; j++)
                {
                    for (int k = 0; k < valuesArray.Length; k++)
                    {
                        if (valuesArray[i] + valuesArray[j] + valuesArray[k] == 2020)
                        {
                            Console.WriteLine(valuesArray[i] * valuesArray[j] * valuesArray[k]);
                            break;
                        }
                    }
                }
            }
        }
    }
}
