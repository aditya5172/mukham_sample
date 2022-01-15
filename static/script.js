function user_attendance()
{
  positivePercent = document.getElementById("positivePercent").value;
  negativePercent = document.getElementById("negativePercent").value;
  console.log(5);
  let attendance_data = {
    labels: ["Present", "Absent"],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [positivePercent, negativePercent],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
  };
  new Chart("user_attendance", {
    type: "doughnut",
    data: attendance_data,
  });
}




console.log(5)
user_attendance();


    //len=document.getElementById("Length").value;
    //console.log("5")
    /*
    var va=[]
    for (let i =1;i<len;i++)
    {
        va[i]=document.getElementById("Week "+i).value;
    }
    console.log(5+3)
    for (let i=0;i<pbs.length;i++)
    {
        l.push(i)
        console.log(l)
    }
*/
/*
const ctx = document.getElementById('myChart').getContext('2d');
let attendance_data =
{
    labels:['1','2'],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [10,30],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
};
const myChart=new Chart(ctx, {
type: "bar",
dataset: attendance_data,
options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


*/
