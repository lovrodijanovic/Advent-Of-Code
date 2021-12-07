using System;
using System.Collections.Generic;

namespace Advent_of_code_d1_1
{
    class Program
    {
        static void Main(string[] args)
        {
            firstPuzzle();
            secondPuzzle();
        }

        static void firstPuzzle()
        {
            int counter = 0;
            List<int> numbers = new List<int>();
            // Read the file and display it line by line.  
            foreach (string line in System.IO.File.ReadLines(@"D:\Advent of Code\2021\Advent-of-code-2021-day1\input.txt"))
            {
                int number = int.Parse(line);
                numbers.Add(number);
            }

            int[] nums = numbers.ToArray();

            for (int i = 1; i < nums.Length; i++)
            {
                if (nums[i] > nums[i - 1])
                {
                    counter++;
                }
            }

            Console.WriteLine(counter);
        }

        static void secondPuzzle()
        {
            int counter = 0;
            List<int> numbers = new List<int>();
            // Read the file and display it line by line.  
            foreach (string line in System.IO.File.ReadLines(@"C:\Users\Loc\Desktop\2021\Advent of Code\Advent-of-code-2021-day1\input.txt"))
            {
                int number = int.Parse(line);
                numbers.Add(number);
            }

            int[] numbersArray = numbers.ToArray();

            List<int> sums = new List<int>();

            for(int i = 0; i < numbersArray.Length-2; i++)
            {
                sums.Add(numbers[i] + numbers[i + 1] + numbers[i + 2]);
            }

            int[] sumsArray = sums.ToArray();

            for(int i = 1; i < sumsArray.Length; i++)
            {
                if(sumsArray[i] > sumsArray[i - 1])
                {
                    counter++;
                }
            }

            Console.WriteLine(counter);

        }
    }
}
