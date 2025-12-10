#!/bin/bash

# Script configuration
set -euo pipefail
IFS=$'\n\t'

# Variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly CONFIG_FILE="${SCRIPT_DIR}/config.sh"
readonly LOG_FILE="/var/log/app.log"

# Environment variables
export NODE_ENV="production"
export DEBUG="${DEBUG:-false}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Functions
log() {
    local level="$1"
    shift
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [${level}] $*" >> "${LOG_FILE}"
}

error() {
    echo -e "${RED}Error: $*${NC}" >&2
    log "ERROR" "$*"
    exit 1
}

success() {
    echo -e "${GREEN}$*${NC}"
    log "INFO" "$*"
}

# Check dependencies
check_deps() {
    local deps=("curl" "jq" "docker")
    for dep in "${deps[@]}"; do
        if ! command -v "$dep" &> /dev/null; then
            error "Required dependency '$dep' not found"
        fi
    done
}

# Main logic
main() {
    check_deps

    # Command line arguments
    while getopts ":hv" opt; do
        case ${opt} in
            h)
                echo "Usage: $0 [-h] [-v]"
                exit 0
                ;;
            v)
                echo "Version 1.0.0"
                exit 0
                ;;
            \?)
                error "Invalid option: -${OPTARG}"
                ;;
        esac
    done

    # Conditionals
    if [[ -f "${CONFIG_FILE}" ]]; then
        source "${CONFIG_FILE}"
    else
        error "Config file not found: ${CONFIG_FILE}"
    fi

    # Loops
    for file in "${SCRIPT_DIR}"/*.sh; do
        echo "Found script: ${file}"
    done

    # Process substitution
    while IFS= read -r line; do
        echo "Processing: ${line}"
    done < <(cat "${CONFIG_FILE}")

    # Command substitution
    local current_date
    current_date=$(date +%Y-%m-%d)

    # Arithmetic
    local count=0
    ((count++))
    result=$((5 + 3 * 2))

    # Arrays
    local -a items=("one" "two" "three")
    echo "First item: ${items[0]}"
    echo "All items: ${items[*]}"
    echo "Count: ${#items[@]}"

    # Associative arrays
    declare -A config
    config[host]="localhost"
    config[port]="8080"

    # Here document
    cat << 'EOF'
This is a here document
with multiple lines
EOF

    success "Script completed successfully"
}

# Run main function
main "$@"
