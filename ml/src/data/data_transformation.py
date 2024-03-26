from typing import Dict
import pandas as pd

from property.schemas import Property


class Transformation:
    @classmethod
    def encode(cls, data: Property) -> Property:
        state_of_building_encoder = {'TO_RESTORE': 1, 'TO_RENOVATE': 2, 'TO_BE_DONE_UP': 3, 'GOOD': 4,
                                     'JUST_RENOVATED': 5, 'AS_NEW': 6}

        kitchen_type_encoder = {'USA_HYPER_EQUIPPED': 3, 'HYPER_EQUIPPED': 3, 'USA_SEMI_EQUIPPED': 2,
                                'SEMI_EQUIPPED': 2, 'USA_INSTALLED': 1, 'INSTALLED': 1, 'USA_UNINSTALLED': 0,
                                'NOT_INSTALLED': 0}

        epc_encoder = {'A++': 9, 'A+': 8, 'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1}

        data.kitchen_type = kitchen_type_encoder.get(data.kitchen_type.upper(), 1)
        data.state_of_building = state_of_building_encoder.get(data.state_of_building.upper(), 0)
        data.epc = epc_encoder.get(data.epc.upper(), 1)
        data.room_count = data.bedroom_count + data.bathroom_count + data.toilet_count
        data.furnished = int(data.furnished)
        data.terrace = int(data.terrace)
        data.garden_exists = int(data.garden_exists)

        return data

    @classmethod
    def transform(cls, data: Property, property_type: str = 'house'):
        data = cls.encode(data=data)
        if property_type == 'house':
            row = {
                'Facades': [data.facades],
                'Habitable Surface': [data.habitable_surface],
                'Land Surface': [data.land_surface],
                'Bedroom Count': [data.bedroom_count],
                'Bathroom Count': [data.bathroom_count],
                'Toilet Count': [data.toilet_count],
                'Room Count': [data.room_count],
                'Kitchen Type': [data.kitchen_type],
                'Furnished': [data.furnished],
                'Terrace': [data.terrace],
                'Garden Exists': [data.garden_exists],
                'State of Building': [data.state_of_building],
                'Living Surface': [data.living_surface],
                'EPC': [data.epc],
                'Consumption Per m2': [data.consumption_per_m2],
                'ANTWERPEN': [1 if data.province == 'ANTWERPEN' else 0],
                'BRUSSEL': [1 if data.province == 'BRUSSEL' else 0],
                'HENEGOUWEN': [1 if data.province == 'HENEGOUWEN' else 0],
                'LIMBURG': [1 if data.province == 'LIMBURG' else 0],
                'LUIK': [1 if data.province == 'LUIK' else 0],
                'LUXEMBURG': [1 if data.province == 'LUXEMBURG' else 0],
                'NAMEN': [1 if data.province == 'NAMEN' else 0],
                'OOST-VLAANDEREN': [1 if data.province == 'OOST-VLAANDEREN' else 0],
                'VLAAMS-BRABANT': [1 if data.province == 'VLAAMS-BRABANT' else 0],
                'WAALS-BRABANT': [1 if data.province == 'WAALS-BRABANT' else 0],
                'WEST-VLAANDEREN': [1 if data.province == 'WEST-VLAANDEREN' else 0]

            }
        else:  # apartment
            row = {
                'Facades': [data.facades],
                'Habitable Surface': [data.habitable_surface],
                'Bedroom Count': [data.bedroom_count],
                'Bathroom Count': [data.bathroom_count],
                'Toilet Count': [data.toilet_count],
                'Room Count': [data.room_count],
                'Kitchen Type': [data.kitchen_type],
                'Furnished': [data.furnished],
                'Terrace': [data.terrace],
                'Terrace Surface': [data.terrace_surface],
                'Garden Exists': [data.garden_exists],
                'State of Building': [data.state_of_building],
                'Living Surface': [data.living_surface],
                'EPC': [data.epc],
                'Consumption Per m2': [data.consumption_per_m2],
                'ANTWERPEN': [1 if data.province.name == 'ANTWERPEN' else 0],
                'BRUSSEL': [1 if data.province.name == 'BRUSSEL' else 0],
                'HENEGOUWEN': [1 if data.province.name == 'HENEGOUWEN' else 0],
                'LIMBURG': [1 if data.province.name == 'LIMBURG' else 0],
                'LUIK': [1 if data.province.name == 'LUIK' else 0],
                'LUXEMBURG': [1 if data.province.name == 'LUXEMBURG' else 0],
                'NAMEN': [1 if data.province.name == 'NAMEN' else 0],
                'OOST-VLAANDEREN': [1 if data.province.name == 'OOST-VLAANDEREN' else 0],
                'VLAAMS-BRABANT': [1 if data.province.name == 'VLAAMS-BRABANT' else 0],
                'WAALS-BRABANT': [1 if data.province.name == 'WAALS-BRABANT' else 0],
                'WEST-VLAANDEREN': [1 if data.province.name == 'WEST-VLAANDEREN' else 0]

            }

        return pd.DataFrame.from_dict(row)
