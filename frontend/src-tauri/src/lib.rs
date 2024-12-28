use tauri::Manager;
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running Tauri application");
}
