using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;

namespace pi
{
    public partial class Form1 : Form
    {
        private HttpClient getPi= new HttpClient();
        private HttpResponseMessage response = new HttpResponseMessage();
        private string pi;
        private int score = 3;
        private Label l1 = new Label();
        private Label l2 = new Label();


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            new Thread(()=> { GetPi("https://uploadbeta.com/api/pi/?cached&n=5000"); }).Start();
            Thread.Sleep(1000);
            affichePi(); // à supprimer
            generateLabels();
            
        }

        private void generateLabels()
        {
            l1.Left = 13;
            l1.Top = 100;
            l1.Width = 320;
            l1.Visible = true;
            l1.ForeColor = Color.Black;
            l1.Text = "pi = 3,";
            Controls.Add(l1);

            l2.Left = 13;
            l2.Top = 125;
            l2.Width = 320;
            l2.Visible = true;
            l2.ForeColor = Color.Black;
            l2.Text = "";
            Controls.Add(l2);
        }

        // test Api -- à supprimer
        private void affichePi()
        {
            label1.Text=pi;
        }

        private async void GetPi(string path)
        {            
            response = await getPi.GetAsync(path);
            if (response.IsSuccessStatusCode)
            {
                pi = await response.Content.ReadAsStringAsync();
            }            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == pi[score].ToString()) {
                if (score < 44) { l1.Text += textBox1.Text; }
                else if (score < 94) { l2.Text += textBox1.Text; }
                
                textBox1.Text = "";
                score++;
            }
            else { gameOver(); }
        }

        private void gameOver()
        {
            BackColor = Color.Red;
            button1.Visible = false;
            textBox1.Visible = false;
            MessageBox.Show("Perdu !");
        }
    }
}
