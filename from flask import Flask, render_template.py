from flask import Flask, render_template, request

app = Flask(__name__)

def generate_crop_advisory(crop: str, soil_type: str) -> str:
    crop = crop.strip().lower() if crop else ""
    soil_type = soil_type.strip().lower() if soil_type else ""
    if not crop or not soil_type:
        return " <strong>Missing Data:</strong> Please select both a crop and a soil type to generate an advisory."

    soil_matrix = {
        "sandy": {
            "warning": "Sandy soil drains rapidly and struggles to retain nutrients. Risk of leaching is high.",
            "tip": "Incorporate organic matter or compost to improve water retention and use split-fertilizer applications."
        },
        "clay": {
            "warning": "Clay soil retains water heavily, leading to poor aeration and high risk of root rot during heavy rains.",
            "tip": "Ensure proper drainage furrows are built, and avoid working the soil when it is completely wet to prevent compaction."
        },
        "loam": {
            "warning": "Loam soil is highly fertile with balanced drainage, but requires regular crop rotation to prevent nutrient depletion.",
            "tip": "Maintain current soil structure with minimal tilling and standard mulching practices."
        },
        "silt": {
            "warning": "Silty soil is fertile but easily compacted and highly prone to water erosion.",
            "tip": "Use cover crops or mulch heavily to protect the topsoil surface from crusting and heavy rainfall impact."
        }
    }

    crop_matrix = {
        "corn": {
            "optimal": ["loam", "silt"],
            "notes": "Corn is a heavy nitrogen feeder and requires deep root penetration."
        },
        "wheat": {
            "optimal": ["loam", "clay"],
            "notes": "Wheat requires stable moisture during early growth but dry conditions near harvest."
        },
        "rice": {
            "optimal": ["clay", "silt"],
            "notes": "Rice thrives in soils with low percolation rates that can hold standing water."
        },
        "soybeans": {
            "optimal": ["loam"],
            "notes": "Soybeans fix their own nitrogen but are sensitive to severe iron deficiencies in highly alkaline soils."
        }
    }

    soil_info = soil_matrix.get(soil_type, {
        "warning": "Localized soil data is limited for this selection.",
        "tip": "Conduct a local soil test to determine organic matter composition."
    })
    
    crop_info = crop_matrix.get(crop, {
        "optimal": [],
        "notes": "Standard crop management practices apply."
    })

    is_optimal = soil_type in crop_info.get("optimal", [])
    
    if is_optimal:
        compatibility_status = " <strong>Optimal Match:</strong> Excellent choice! This soil type naturally supports the root architecture and moisture needs of this crop."
    elif soil_type == "sandy" and crop in ["corn", "rice"]:
        compatibility_status = " <strong>High Risk Warning:</strong> This is a poor combination. Sandy soil drains too quickly for water-intensive crops like rice, and will leach the heavy nitrogen required by corn."
    elif soil_type == "clay" and crop == "wheat":
        compatibility_status = " <strong>Moderate Risk Warning:</strong> Clay retains too much water, which can stunt wheat root development and encourage fungal diseases during wet seasons."
    else:
        compatibility_status = " <strong>Sub-Optimal Match:</strong> While manageable, this soil type is not ideal for this crop. Success will require strict intervention and modified irrigation."

    advisory_html = f"""
    <div class="advisory-result">
        <h3>🌾 Custom Advisory Report: {crop.title()} in {soil_type.title()} Soil</h3>
        <hr>
        <p>{compatibility_status}</p>
        
        <div class="advisory-section">
            <strong> Localized Soil Risk:</strong> {soil_info['warning']}
        </div>
        
        <div class="advisory-section" style="margin-top: 10px;">
            <strong> Management Action:</strong> {soil_info['tip']}
        </div>
        
        <div class="advisory-section" style="margin-top: 10px;">
            <strong> Crop-Specific Notes:</strong> {crop_info['notes']}
        </div>
    </div>
    """
    return advisory_html


@app.route('/get-advisory', methods=['POST'])
def advisory_endpoint():
    selected_crop = request.form.get('crop')
    selected_soil = request.form.get('soil_type')
    
    final_advisory = generate_crop_advisory(selected_crop, selected_soil)
    return render_template('advisory.html', advisory_data=final_advisory)

if __name__ == '__main__':
    app.run(debug=True)