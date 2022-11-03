from pypodio2 import api

import json

podio = api.OAuthClient(
    'acquisition-leads-allocation',
    '63dh8L5uBLLz9FYo0pVIbl991waGwyqQ3Vd2H6Vje5oM5gmAEYo5VhUUWh9LLUtJ',
    'deepeshnfs462@gmail.com',
    'Fm=e=Z3h1',
)

y = podio.Item.filter_by_view(25307577, 54878767, limit=500)["items"]
print(len(y))

row_ = 2
import csv
with open("C:/Users/ADMIN/Downloads/podio-data.csv", 'w', newline='') as csvfile:
    podiowriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    podiowriter.writerow(['name', 'property_address', 'phone', 'lead_manager', 'lead_status_d_t', 'lead_status_note', 'lead_disposition'])
    
    for x in y:

        name = property_address = phone = lead_manager = lead_status_d_t = lead_status_note = lead_disposition = ""

        for i in x["fields"]:
            #     print(i)
            if i["field_id"] == 214922599:
                name = i["values"][0].get("value")
            elif i["field_id"] == 214922613:
                property_address = i["values"][0].get("value")
            elif i["field_id"] == 214922601:
                phone = i["values"][0].get("value")
            elif i["field_id"] == 216652314:
                lead_manager = i["values"][0].get("value")["text"]
            elif i["field_id"] == 214922608:
                lead_status_d_t = i["values"][0].get("value")
            elif i["field_id"] == 215340656:
                lead_status_note = i["values"][0].get("value")
            elif i["field_id"] == 229837786:
                lead_disposition = i["values"][0].get("value")
            #       ----
            #         elif i["field_id"]==214922643:
            #             zillow_link = i["values"][0].get("value")
            #         elif i["field_id"]==214922611:
            #             sms_status = i["values"][0].get("value")
            #         elif i["field_id"]==214922602:
            #             sellers_email = i["values"][0].get("value")
            #         elif i["field_id"]==230504670:
            #             language = i["values"][0].get("value")
            #         elif i["field_id"]==214922612:
            #             motivation_bucket = i["values"][0].get("value")
            #         elif i["field_id"]==214922607:
            #             call_track = i["values"][0].get("value")
            #         elif i["field_id"]==214922618:
            #             property_type = i["values"][0].get("value")
            #         elif i["field_id"]==214922619:
            #             bedrooms = i["values"][0].get("value")
            #         elif i["field_id"]==214922620:
            #             bathrooms = i["values"][0].get("value")
            #         elif i["field_id"]==214922630:
            #             sqft = i["values"][0].get("value")
            #         elif i["field_id"]==214922632:
            #             year_built = i["values"][0].get("value")
            #         elif i["field_id"]==214922629:
            #             general_notes = i["values"][0].get("value")
            #         elif i["field_id"]==216488280:
            #             pool = i["values"][0].get("value")
            #         elif i["field_id"]==216488281:
            #             garage = i["values"][0].get("value")
            #         elif i["field_id"]==216488282:
            #             occupancy = i["values"][0].get("value")
            #         elif i["field_id"]==216530760:
            #             ac = i["values"][0].get("value")
            #         elif i["field_id"]==216488286:
            #             water_heater = i["values"][0].get("value")
            #         elif i["field_id"]==216488288:
            #             plumbing = i["values"][0].get("value")
            #         elif i["field_id"]==216488292:
            #             kitchen = i["values"][0].get("value")
            #         elif i["field_id"]==216488293:
            #             other_updates = i["values"][0].get("value")
            #         elif i["field_id"]==216488294:
            #             repairs_needed = i["values"][0].get("value")
            #         elif i["field_id"]==216488290:
            #             reason_for_selling = i["values"][0].get("value")
            #         elif i["field_id"]==216488295:
            #             price_expectation = i["values"][0].get("value")
            else: pass
        print(name, property_address, phone, lead_manager, lead_status_d_t, lead_status_note, lead_disposition,
              end="\n \n \n")
    #     sheet.update_cell(row_, 1, name)
    #     sheet.update_cell(row_, 2, property_address)
    #     sheet.update_cell(row_, 3, phone)
    #     sheet.update_cell(row_, 4, lead_manager)
    #     sheet.update_cell(row_, 5, lead_status_d_t)
    #     sheet.update_cell(row_, 6, lead_status_note)
    #     sheet.update_cell(row_, 7, lead_disposition)
        podiowriter.writerow([name, property_address, phone, lead_manager, lead_status_d_t, lead_status_note, lead_disposition])
        row_ += 1
