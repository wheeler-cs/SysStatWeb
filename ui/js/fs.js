
async function fetchDiskUsage()
{
    try
    {
        const response = await fetch("http://localhost:9595/fs/percent-used");
        if(!response.ok)
        {
            throw new Error("Could not contact usage endpoint: ${reponse.status}");
        }
        const data = await response.json();
        document.getElementById("diskusage").value = data["message"]
        console.log(data["message"]);
    }
    catch (error)
    {
        console.error("Fetch disk usage failed", error);
    }
}

document.addEventListener("DOMContentLoaded", () =>
{
    fetchDiskUsage();
});
