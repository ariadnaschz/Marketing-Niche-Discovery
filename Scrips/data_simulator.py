import pandas as pd
import numpy as np
import os

def simulate_niche_scenario(input_path, output_path):
    print("Cargando dataset base...")
    df = pd.read_csv(input_path)
    
    # Limpieza inicial básica
    df['Acquisition_Cost'] = df['Acquisition_Cost'].replace('[\$,]', '', regex=True).astype(float)
    df['Conversion_Rate'] = pd.to_numeric(df['Conversion_Rate'], errors='coerce')
    clicks = pd.to_numeric(df['Clicks'], errors='coerce')
    impressions = pd.to_numeric(df['Impressions'], errors='coerce').replace(0, np.nan)
    ctr = (clicks / impressions).fillna(0)
    
    np.random.seed(42) # Para que siempre nos dé la misma historia
    print("Inyectando reglas de negocio...")
    
    # 1. Regla Base de Conversión dependiente del CTR
    df['Conversion_Rate'] = (df['Conversion_Rate'].fillna(0.02) * 0.5) + (ctr * 0.4) + np.random.normal(0, 0.01, len(df))
    
    # 2. EL AGUJERO NEGRO (Mucho gasto, mala eficiencia)
    # Supongamos que la empresa ama gastar en Facebook para 'Fashionistas', pero ya hay fatiga de anuncios
    mask_black_hole = (df['Channel_Used'] == 'Facebook') & (df['Customer_Segment'] == 'Fashionistas')
    df.loc[mask_black_hole, 'Acquisition_Cost'] *= 1.8 # Los costos se disparan
    df.loc[mask_black_hole, 'Conversion_Rate'] *= 0.6  # La gente ya no convierte
    
    # 3. LA MINA DE ORO OCULTA (El Nicho)
    # 'Tech Enthusiasts' a través de 'Email' es baratísimo y convierte brutal, pero gastamos poco ahí
    mask_gold_mine = (df['Channel_Used'] == 'Email') & (df['Customer_Segment'] == 'Tech Enthusiasts')
    df.loc[mask_gold_mine, 'Acquisition_Cost'] *= 0.4 # Costos bajísimos
    df.loc[mask_gold_mine, 'Conversion_Rate'] *= 1.5  # Alta conversión
    
    # Limitar el Conversion Rate a niveles realistas (1% a 25%)
    df['Conversion_Rate'] = df['Conversion_Rate'].clip(0.01, 0.25)
    
    # 4. Calcular Métricas Finales
    df['Conversions'] = (df['Clicks'] * df['Conversion_Rate']).clip(lower=1)
    
    value_map = {
        'Tech Enthusiasts': 300,
        'Foodies': 150,
        'Fashionistas': 200,
        'Health & Wellness': 250,
        'Outdoor Adventurers': 180
    }
    df['Value_per_Conversion'] = df['Customer_Segment'].map(value_map)
    df['Revenue'] = df['Conversions'] * df['Value_per_Conversion'] * np.random.uniform(0.9, 1.1, len(df))
    
    df['CPA'] = df['Acquisition_Cost'] / df['Conversions']
    df['ROI'] = (df['Revenue'] - df['Acquisition_Cost']) / df['Acquisition_Cost']
    
    # Limpieza final de infinitos
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(subset=['CPA', 'ROI'], inplace=True)
    
    # Guardar el dataset listo para el Dashboard
    df.to_csv(output_path, index=False)
    print(f"✅ Simulación completada. Archivo guardado en: {output_path}")

# Ejecución
if __name__ == "__main__":
    # 1. Obtenemos la ruta exacta de la carpeta donde está guardado este script (la carpeta 'scripts')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Subimos un nivel para llegar a la raíz de tu proyecto
    project_root = os.path.dirname(script_dir)
    
    # 3. Construimos las rutas dinámicamente hacia tus carpetas de datos
    data_dir = os.path.join(project_root, "Data")
    input_file = os.path.join(data_dir, "marketing_campaign_dataset.csv")
    output_file = os.path.join(data_dir, "marketing_simulated_niche.csv")

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {input_file}")

    # 4. Si la carpeta de salida no existe, la creamos automáticamente
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # 5. Ejecutamos la simulación
    print(f"Ruta de lectura: {input_file}")
    simulate_niche_scenario(input_file, output_file)
