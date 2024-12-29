use tauri::Manager;
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| Ok(()))
        .run(tauri::generate_context!())
        .expect("error while running Tauri application");
}
