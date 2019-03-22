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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            new Thread(()=> { GetPi("https://uploadbeta.com/api/pi/?cached&n=5000"); }).Start();
            Thread.Sleep(1000);
            affichePi();
        }

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

    }
}
