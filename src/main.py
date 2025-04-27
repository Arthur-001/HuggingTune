import flet as ft
import json

def main(page: ft.Page):
    # Set dark theme
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "LLM Customization App"
    page.window_width = 900
    page.window_height = 650
    
    # Define the Dataset module
    def dataset_view():
        # Variables to hold the dataset
        dataset_text = ft.TextField(
            multiline=True,
            min_lines=10,
            max_lines=20,
            expand=True,
            label="Enter JSON Dataset",
            hint_text='{"example": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]}',
            border=ft.InputBorder.OUTLINE,
        )
        
        status_text = ft.Text("Ready to load JSON data", color=ft.colors.GREEN)
        
        # Function to validate JSON
        def validate_json(e):
            try:
                if dataset_text.value:
                    json_data = json.loads(dataset_text.value)
                    status_text.value = f"✓ Valid JSON: {len(json_data)} top-level items"
                    status_text.color = ft.colors.GREEN
                else:
                    status_text.value = "Please enter some JSON data"
                    status_text.color = ft.colors.YELLOW
            except json.JSONDecodeError as err:
                status_text.value = f"❌ Invalid JSON: {str(err)}"
                status_text.color = ft.colors.RED
            page.update()
        
        # Function to clear the text field
        def clear_dataset(e):
            dataset_text.value = ""
            status_text.value = "Dataset cleared"
            status_text.color = ft.colors.YELLOW
            page.update()
        
        # Return the dataset view
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_color=ft.colors.BLUE_200,
                        tooltip="Back to Home",
                        on_click=lambda e: navigate_to("home")
                    ),
                    ft.Text("Dataset Manager", size=24, weight=ft.FontWeight.BOLD),
                ]),
                ft.Text("Enter your dataset in JSON format below:", size=16),
                dataset_text,
                ft.Row([
                    ft.ElevatedButton("Validate JSON", on_click=validate_json, icon=ft.icons.CHECK),
                    ft.OutlinedButton("Clear", on_click=clear_dataset, icon=ft.icons.CLEAR),
                ]),
                status_text,
            ]),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.SURFACE_VARIANT,
            margin=10,
            expand=True
        )

    # Define the Home view
    def home_view():
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text(
                        "Welcome to LLM Customization App",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE_200,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=40, bottom=40),
                ),
                ft.Container(
                    content=ft.Text(
                        "This application helps you customize and train language models with your own data.",
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    margin=ft.margin.only(bottom=30),
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Icon(ft.icons.DATASET, size=60, color=ft.colors.BLUE_400),
                                    ft.Text("Dataset", size=20, weight=ft.FontWeight.W_500),
                                    ft.Text("Manage your JSON datasets for training"),
                                    ft.ElevatedButton(
                                        "Open Dataset Manager",
                                        icon=ft.icons.ARROW_FORWARD,
                                        on_click=lambda e: navigate_to("dataset")
                                    )
                                ]),
                                padding=20,
                                alignment=ft.alignment.center,
                            ),
                            elevation=5,
                            width=250,
                            height=250,
                        ),
                        # Placeholder for future sections/cards
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Icon(ft.icons.SETTINGS, size=60, color=ft.colors.ORANGE_400),
                                    ft.Text("Configuration", size=20, weight=ft.FontWeight.W_500),
                                    ft.Text("Coming soon..."),
                                ]),
                                padding=20,
                                alignment=ft.alignment.center,
                            ),
                            elevation=5,
                            width=250,
                            height=250,
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Icon(ft.icons.SMART_TOY, size=60, color=ft.colors.GREEN_400),
                                    ft.Text("Training", size=20, weight=ft.FontWeight.W_500),
                                    ft.Text("Coming soon..."),
                                ]),
                                padding=20,
                                alignment=ft.alignment.center,
                            ),
                            elevation=5,
                            width=250,
                            height=250,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
            ]),
            padding=20,
            expand=True,
        )

    # Container to hold the current view
    content_container = ft.Container(expand=True)

    # Navigation function
    def navigate_to(view_name):
        content_container.content = views[view_name]
        page.update()

    # Define available views
    views = {
        "home": home_view(),
        "dataset": dataset_view(),
    }

    # Initialize with home view
    content_container.content = views["home"]

    # Add content to page
    page.add(content_container)

ft.app(target=main)