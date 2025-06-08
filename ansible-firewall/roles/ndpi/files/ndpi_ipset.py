#!/usr/bin/env python3
import sys
import json
import subprocess

# Mapping of nDPI application/category names to ipset names
NDPI_MAP = {
    "Zoom": "ndpi_app_zoom",
    "Microsoft Teams": "ndpi_app_microsoft_teams",
    "VoIP": "ndpi_category_voip",
    "VPN": "ndpi_category_vpn",
    "Riot Games": "ndpi_app_riot_games",
    "YouTube": "ndpi_app_youtube",
    "Netflix": "ndpi_app_netflix",
    "Amazon Prime Video": "ndpi_app_amazon_prime_video",
    "BitTorrent": "ndpi_app_bittorrent",
}

TIMEOUT = "300"

for line in sys.stdin:
    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        continue
    app = data.get("master") or data.get("app_protocol")
    category = data.get("category")
    src = data.get("src_ip")
    dst = data.get("dst_ip")

    for name, ipset in NDPI_MAP.items():
        if app == name or category == name:
            for ip in (src, dst):
                if not ip:
                    continue
                subprocess.run([
                    "ipset", "add", ipset, ip, "timeout", TIMEOUT
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            break
