// SimplifiedBlocks JSON Editor with Monaco

let editor = null;
let templates = [];
let currentConfig = null;
let showDefaults = true;

// Initialize Monaco Editor
require.config({ paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs' } });

require(['vs/editor/editor.main'], async function() {
    await init();
});

async function init() {
    // Load templates
    await loadTemplates();

    // Initialize Monaco Editor
    initEditor();

    // Setup event listeners
    setupEventListeners();

    // Load default template
    loadDefaultConfig();
}

// Initialize Monaco Editor
function initEditor() {
    // Create editor instance
    editor = monaco.editor.create(document.getElementById('editor-container'), {
        value: '{}',
        language: 'json',
        theme: 'vs-dark',
        automaticLayout: true,
        minimap: { enabled: false },
        fontSize: 14,
        formatOnPaste: true,
        formatOnType: true,
        scrollBeyondLastLine: false,
    });

    // Listen for content changes
    editor.onDidChangeModelContent(() => {
        validateJSON();
    });
}

// Load templates from backend
async function loadTemplates() {
    try {
        const response = await fetch('/simplified_templates');
        const data = await response.json();
        templates = data.templates;

        populateTemplateSelect();
    } catch (error) {
        console.error('Failed to load templates:', error);
    }
}

// Populate template selector
function populateTemplateSelect() {
    const select = document.getElementById('templateSelect');

    templates.forEach((template, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = `${template.name} - ${template.description}`;
        select.appendChild(option);
    });
}

// Setup event listeners
function setupEventListeners() {
    const templateSelect = document.getElementById('templateSelect');
    const loadTemplateBtn = document.getElementById('loadTemplateBtn');
    const showDefaultsToggle = document.getElementById('showDefaultsToggle');
    const validateBtn = document.getElementById('validateBtn');
    const formatBtn = document.getElementById('formatBtn');
    const clearBtn = document.getElementById('clearBtn');
    const buildBtn = document.getElementById('buildBtn');
    const saveBtn = document.getElementById('saveBtn');
    const loadBtn = document.getElementById('loadBtn');

    templateSelect.addEventListener('change', (e) => {
        loadTemplateBtn.disabled = !e.target.value;
    });

    loadTemplateBtn.addEventListener('click', loadSelectedTemplate);
    showDefaultsToggle.addEventListener('change', toggleDefaults);
    validateBtn.addEventListener('click', () => validateJSON());
    formatBtn.addEventListener('click', formatJSON);
    clearBtn.addEventListener('click', clearEditor);
    buildBtn.addEventListener('click', buildCharacter);
    saveBtn.addEventListener('click', saveConfiguration);
    loadBtn.addEventListener('click', loadConfiguration);
}

// Load default config
function loadDefaultConfig() {
    const defaultConfig = {
        "block_type": "SimplifiedBlocks",
        "classes": {
            "class_levels": {
                "WIZARD": 1
            }
        }
    };

    currentConfig = defaultConfig;
    editor.setValue(JSON.stringify(defaultConfig, null, 2));
}

// Load selected template
function loadSelectedTemplate() {
    const select = document.getElementById('templateSelect');
    const index = parseInt(select.value);

    if (isNaN(index)) return;

    const template = templates[index];
    const config = showDefaults ? template.config_with_defaults : template.config;

    currentConfig = config;
    editor.setValue(JSON.stringify(config, null, 2));
}

// Toggle between showing/hiding defaults
async function toggleDefaults(e) {
    showDefaults = e.target.checked;

    // If a template is selected, reload it with new display mode
    const select = document.getElementById('templateSelect');
    if (select.value) {
        loadSelectedTemplate();
    } else {
        // Try to parse current editor content and reformat it
        try {
            const current = JSON.parse(editor.getValue());

            // Call backend to validate and reformat with or without defaults
            const formatted = await formatWithDefaults(current, showDefaults);
            if (formatted) {
                editor.setValue(JSON.stringify(formatted, null, 2));
            }
        } catch (error) {
            // Invalid JSON, do nothing
            console.error('Failed to toggle defaults:', error);
        }
    }
}

// Format config with or without defaults via backend
async function formatWithDefaults(config, showDefaults) {
    try {
        const response = await fetch(`/format_simplified?show_defaults=${showDefaults}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(config)
        });

        if (response.ok) {
            return await response.json();
        } else {
            console.error('Format failed:', await response.text());
            return null;
        }
    } catch (error) {
        console.error('Failed to format:', error);
        return null;
    }
}

// Validate JSON
function validateJSON() {
    const statusDiv = document.getElementById('validation-status');

    try {
        const json = JSON.parse(editor.getValue());

        // Basic validation checks
        if (!json.block_type || json.block_type !== 'SimplifiedBlocks') {
            throw new Error('block_type must be "SimplifiedBlocks"');
        }

        if (!json.classes || !json.classes.class_levels) {
            throw new Error('classes.class_levels is required');
        }

        // Success
        statusDiv.className = 'validation-status success';
        statusDiv.textContent = '✓ Valid SimplifiedBlocks configuration';
        return true;
    } catch (error) {
        statusDiv.className = 'validation-status error';
        statusDiv.textContent = `✗ ${error.message}`;
        return false;
    }
}

// Format JSON
function formatJSON() {
    try {
        const json = JSON.parse(editor.getValue());
        editor.setValue(JSON.stringify(json, null, 2));
    } catch (error) {
        alert('Cannot format invalid JSON');
    }
}

// Clear editor
function clearEditor() {
    if (confirm('Clear all configuration?')) {
        loadDefaultConfig();
    }
}

// Build character
async function buildCharacter() {
    const buildOutput = document.getElementById('buildOutput');
    const buildResults = document.getElementById('buildResults');

    // Validate first
    if (!validateJSON()) {
        alert('Please fix validation errors before building');
        return;
    }

    const config = JSON.parse(editor.getValue());

    buildOutput.innerHTML = '<div class="loading">Building character...</div>';
    buildResults.style.display = 'block';
    buildResults.scrollIntoView({ behavior: 'smooth' });

    try {
        const response = await fetch('/create_character', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                building_blocks: config,
                increment_chain: {}
            })
        });

        const result = await response.json();

        if (response.ok && result.character) {
            buildOutput.innerHTML = `
                <div class="success">
                    <h3>✅ Character Created Successfully!</h3>
                    <div class="character-summary">
                        <p><strong>Name:</strong> ${result.character.name || 'N/A'}</p>
                        <p><strong>Race:</strong> ${result.character.race || 'N/A'}</p>
                        <p><strong>Level:</strong> ${result.character.level || 'N/A'}</p>
                        <p><strong>Classes:</strong> ${formatClasses(result.character.classes)}</p>
                    </div>
                    <details>
                        <summary>View Full Character JSON</summary>
                        <pre>${JSON.stringify(result.character, null, 2)}</pre>
                    </details>
                    <details>
                        <summary>View Increment Chain</summary>
                        <pre>${JSON.stringify(result.increment_chain, null, 2)}</pre>
                    </details>
                </div>
            `;
        } else {
            buildOutput.innerHTML = `
                <div class="error">
                    <h3>❌ Build Failed</h3>
                    <pre>${result.detail || result.error || JSON.stringify(result, null, 2)}</pre>
                </div>
            `;
        }
    } catch (error) {
        buildOutput.innerHTML = `
            <div class="error">
                <h3>❌ Error</h3>
                <p>${error.message}</p>
            </div>
        `;
    }
}

// Format classes for display
function formatClasses(classes) {
    if (!classes) return 'N/A';
    return Object.entries(classes)
        .map(([cls, level]) => `${cls} ${level}`)
        .join(', ');
}

// Save configuration to localStorage
function saveConfiguration() {
    if (!validateJSON()) {
        alert('Cannot save invalid configuration');
        return;
    }

    const config = editor.getValue();
    const name = prompt('Configuration name:');
    if (name) {
        localStorage.setItem(`simplified_config_${name}`, config);
        alert('✅ Configuration saved!');
    }
}

// Load configuration from localStorage
function loadConfiguration() {
    const configs = Object.keys(localStorage)
        .filter(k => k.startsWith('simplified_config_'))
        .map(k => k.replace('simplified_config_', ''));

    if (configs.length === 0) {
        alert('No saved configurations found');
        return;
    }

    const name = prompt(`Available configs:\n${configs.join('\n')}\n\nEnter name to load:`);
    if (name) {
        const config = localStorage.getItem(`simplified_config_${name}`);
        if (config) {
            editor.setValue(config);
        }
    }
}
