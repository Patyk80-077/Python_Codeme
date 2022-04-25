import day_temp
import requests
import json
from datetime import datetime
from fpdf import FPDF


def print_day(pdf,day):
    pdf.add_page()
    pdf.set_font('Arial','B',16)

    pdf.cell(60,20,f"Date: {day['date']}",0,1,'C')
    pdf.cell(40,10, f"\tsunrise: {day['sunrise']}",0,1)
    pdf.cell(40,10,f"\tsunset: {day['sunset']}",0,1)
    pdf.cell(40,10,f"\tminimal temperature: {day['tmin']}",0,1)
    pdf.cell(40,10,f"\tmaximal temperature: {day['tmax']}",0,1)
    pdf.cell(40,10,f"\ttemperature during the day: {day['tday']}",0,1)
    pdf.cell(40,10,f"\ttemperature at night: {day['tnight']}",0,1)
    pdf.cell(40,10,f"\tweather: {day['weather']}",0,1)
    pdf.cell(40,10,f"\tpressure: {day['pressure']}",0,1)
    pdf.cell(40,10,f"\thumidity: {day['humidity']}",0,1)
    pdf.cell(40,10,f"\twind speed: {day['wind_speed']}",0,1)
    pdf.cell(40,10,f"\tcloudiness: {day['cloudiness']}",0,1)
    return pdf