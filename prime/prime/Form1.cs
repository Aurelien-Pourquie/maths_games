using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prime
{
    public partial class Form1 : Form
    {
        int lastnumber = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int input = Convert.ToInt32(textBox1.Text);

            // 2 is prime
            if (lastnumber == 0)
            {
                if (input == 2)
                {
                    BackColor = Color.Blue;
                    listBox1.Items.Add(input);
                    lastnumber = input;
                    textBox1.Text = "";
                }
                else { gameover(); }
            }

            else if (checkRange(input))
            {
                if (checkPrime(input))
                {
                    if (checkIsNext(input))
                    {
                        BackColor = Color.Blue;
                        listBox1.Items.Add(input);
                        lastnumber = input;
                        textBox1.Text = "";
                    }
                    else { gameover(); }
                }
                else { gameover(); }
            }
            else { gameover(); }
        }        

        private bool checkRange(int input)
        {          

            if (input > lastnumber)
            {
                return true;
            }
            else { return false; }
        }

        private bool checkPrime(int input)
        {
            for (int i = 2; i < input; i++)
            {
                if (input % i == 0)
                {
                   return false;                   
                }
            }
            return true;
        }

        private bool checkIsNext(int input)
        {
            for (int i = lastnumber+1; i < input; i++)
            {
                if (checkPrime(i)) { return false; }
            }
            return true;
        }

        private void gameover()
        {
            BackColor = Color.Red;
            button1.Visible = false;
            textBox1.Visible = false;
            MessageBox.Show("Perdu !");
        }
    }
}
