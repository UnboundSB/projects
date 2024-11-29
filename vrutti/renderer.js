//Open Folders
document.getElementById('open-folder-btn').addEventListener('click', async () => {
    const folderPaths = await window.electronAPI.openDialog();
    console.log("Selected folder:", folderPaths);
    if (folderPaths.length > 0) {
        alert("Selected: " + folderPaths.join(", "));
    } else {
        alert("No file selected.");
    }
});
// Open Files
document.getElementById('open-file-btn').addEventListener('click', async () => {
    const filePaths = await window.electronAPI.openDialog();
    console.log("Selected Files:", filePaths);
    if (filePaths.length > 0) {
        alert("Selected: " + filePaths.join(", "));
    } else {
        alert("No file selected.");
    }
});
