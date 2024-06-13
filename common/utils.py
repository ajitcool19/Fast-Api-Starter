from typing import Union

def to_camel_case(string: str) -> str:
    components = string.split('_')
    return components[0] + ''.join(_.capitalize() for _ in components[1:])


def get_available_statuses():
    return {
        1: 'In Draft',
        2: 'Submitted',
        3: 'Approved',
        4: 'Rejected',
        5: 'Needs Resubmission',
        6: 'Deactivated',
        7: 'Partially raised',
        8: 'Raised',
        9: 'Partially accepted',
        10: 'Accepted',
        11: 'Checked In',
        12: 'Checked Out',
        13: 'Vehicle Breakdown',
        14: 'Forced Check Out',
        15: 'Temporary',
        16: 'Completed'
    }


def get_ownership_mapping():
    return {
        1: 'moeving',
        2: 'leased',
        3: 'dco'
    }


def get_language_mapping():
    return {
        1: 'Hindi',
        2: 'English',
        3: 'Bangla',
        4: 'Tamil',
        5: 'Telugu',
        6: 'kannada',
    }


def map_unique_languages(language: Union[int, str]) -> Union[str, int]:
    if not language:
        return
    available_mappings = get_language_mapping()

    by_value = False
    if isinstance(language, str):
        by_value = True

    if by_value:
        for language_number, language_value in available_mappings.items():
            if language_value.lower() == language.lower():
                return language_number
    if int(language) in available_mappings:
        return available_mappings[int(language)]


def map_unique_ownership(ownership: Union[int, str]) -> Union[str, int]:
    available_mappings = get_ownership_mapping()

    by_value = False
    if isinstance(ownership, str):
        by_value = True

    if by_value:
        for ownership_number, ownership_value in available_mappings.items():
            if ownership_value.lower() == ownership.lower():
                return ownership_number
    return available_mappings[int(ownership)]


def map_unique_moeving_statuses(status: Union[int, str]) -> Union[str, int]:
    available_statuses = get_available_statuses()

    by_value = False
    if isinstance(status, str):
        by_value = True

    if by_value:
        for status_number, status_value in available_statuses.items():
            if status_value.lower() == status.lower().replace('_', ' '):
                return status_number

    return available_statuses[int(status)]


def map_date_pattern(value: Union[int, str]) -> Union[str, int]:
    by_value = False
    if isinstance(value, str):
        by_value = True

    patterns = {
        1: 'RANGE',
        2: 'RANDOM_DATES'
    }

    if by_value:
        for k, v in patterns.items():
            if v.upper() == value.upper():
                return k

    return patterns[value]


def map_user_role(value: Union[int, str]) -> Union[str, int]:
    by_value = False
    if isinstance(value, str):
        by_value = True

    patterns = {
        1: 'admin',
        2: 'entrepreneur',
        3: 'driver',
        4: 'both',
        5: 'pseudo_login',
        6: 'driver editor'
    }

    if by_value:
        for k, v in patterns.items():
            if v.upper() == value.upper():
                return k

    return patterns[value]


# demand slot audit logs
demand_slot_audit_log_op_id = {
    "DRIVER_CHECK_IN": 101,
    "DRIVER_CHECK_OUT": 102,
    "EDIT_CHECK_IN_OUT": 103,

    "FORCED_CHECK_OUT_CHANGE_VEHICLE_ASSIGNED_TO_DEMAND": 104,
    "FORCED_CHECK_OUT_UNASSIGN_DRIVER_FROM_VEHICLE": 105,

    "FORCED_CHECK_OUT_CHANGE_OF_ENTP_OF_VEHICLE": 106,
    "FORCED_CHECK_OUT_CHANGE_OF_CITY_OF_VEHICLE": 107,
    "FORCED_CHECK_OUT_CHANGE_OF_ENTP_OF_DRIVER": 108,
    "FORCED_CHECK_OUT_CHANGE_OF_CITY_OF_DRIVER": 109,

    "FORCED_CHECK_OUT_REJECT_ENTP_DEMAND": 110,
    "FORCED_CHECK_OUT_DEACTIVATE_DEMAND": 111,
    "FORCED_CHECK_OUT_CANCEL_ALLOCATION_ENTP_DEMAND": 112
}


def map_dco_attendance_type(value: Union[int, str]) -> Union[str, int]:
    by_value = False
    if isinstance(value, str):
        by_value = True

    patterns = {
        1: 'FP',  # full present - dco vehicle driven by dco driver
        2: 'DM',  # Driver Missing - dco vehicle driven by non dco driver ( so then the dco gets paid for renting out
        # their vehicle)
        3: 'DP',  # Driver Present - dco driver delivers using a moeving vehicle and not their vehicle (dco gets paid
        # for delivery minus the vehicle rent)
        4: 'MD',  # Moeving Driver driving Moeving vehicle
    }

    if by_value:
        for k, v in patterns.items():
            if v.upper() == value.upper():
                return k

    return patterns[value]


def map_ledger_transaction_type(value: Union[int, str]) -> Union[str, int]:
    by_value = False
    if isinstance(value, str):
        by_value = True

    patterns = {
        1: 'Credit',
        2: 'Debit',
    }

    if by_value:
        for k, v in patterns.items():
            if v.upper() == value.upper():
                return k

    return patterns[value]


#   vehicle breakdown audit logs

# vehicle_breakdown_audit_log_op_id = {
#     "VEHICLE_IS_BACK_FROM_MAINTENANCE": 0,
#     "VEHICLE_IS_DOWN_FOR_MAINTENANCE BUT CAN WORK": 1,
#     "VEHICLE_IS_DOWN_FOR_MAINTENANCE BUT CAN'T WORK": 2,
# }

def map_vehicle_breakdown_audit_log_op_id(value: Union[int, str]) -> Union[str, int]:
    by_value = False
    if isinstance(value, str):
        by_value = True

    op_status = {
        0: "VEHICLE_IS_BACK_FROM_MAINTENANCE",
        1: "VEHICLE_IS_DOWN_FOR_MAINTENANCE_BUT_CAN_WORK",
        2: "VEHICLE_IS_DOWN_FOR_MAINTENANCE_BUT_CAN'T_WORK",

    }
    if by_value:
        for k, v in op_status.items():
            if v.upper() == value.upper():
                return k

    return op_status[value]


def map_vehicle_ownership_by_id(value: Union[int, str]) -> Union[str, int]:
    by_value = False
    if isinstance(value, str):
        by_value = True

    ownership_status = {
        1: "MOEVING",
        2: "LEASED",
        3: "DCO",

    }
    if by_value:
        for k, v in ownership_status.items():
            if v.upper() == value.upper():
                return k

    return ownership_status[value]


def finance_master(finance_master):
    ownership_id = finance_master.vehicle_ownership_id
    ownership_subtype_id = finance_master.vehicle_ownership_subtype_id
    finance_provider_id = finance_master.vehicle_finance_provider_id

    vehicle_ownership = None
    vehicle_ownership_subtype = None
    finance_provider = None
    vehicle_lease_provider = None

    master_list = [
        {
            "vehicleOwnershipId": 1,
            "vehicleOwnershipType": "moeving",
            "vehicleOwnershipSubtypes": [
                {
                    "vehicleOwnershipSubTypeId": 1,
                    "vehicleOwnershipSubType": "OWN",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 2,
                    "vehicleOwnershipSubType": "LOAN",
                    "vehicleFinanceOptions": [
                        {
                            "financeProviderId": 1,
                            "financeProviderName": "EDUVANZ FINANCING PRIVATE LIMITED"
                        },
                        {
                            "financeProviderId": 2,
                            "financeProviderName": "CKERS FINANCE LIMTIED"
                        },
                        {
                            "financeProviderId": 3,
                            "financeProviderName": "SUNDARAM FIANNCE LIMITED"
                        },
                        {
                            "financeProviderId": 4,
                            "financeProviderName": "IDFC FIRST BANK"
                        },
                        {
                            "financeProviderId": 5,
                            "financeProviderName": "AMU LEASING PVT LTD"
                        },
                        {
                            "financeProviderId": 6,
                            "financeProviderName": "ANANYA FINANCE"
                        },
                        {
                            "financeProviderId": 7,
                            "financeProviderName": "HDFC BANK LTD"
                        }
                    ]
                }
            ]
        },
        {
            "vehicleOwnershipId": 2,
            "vehicleOwnershipType": "leased",
            "vehicleOwnershipSubtypes": [
                {
                    "vehicleOwnershipSubTypeId": 3,
                    "vehicleOwnershipSubType": "OTO CAPITAL -1T9 TECHNOLOGY PRIVATE LIMITED",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 4,
                    "vehicleOwnershipSubType": "OTO CAPITAL -CKERS FINANCE LIMITED",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 5,
                    "vehicleOwnershipSubType": "OTO CAPITAL - NOTHERN ARC CAOITAL PVT LTD",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 6,
                    "vehicleOwnershipSubType": "OTO CAPITAL ",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 7,
                    "vehicleOwnershipSubType": "TWU-SHABRI INVESTMENTS PVT.LTD",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 8,
                    "vehicleOwnershipSubType": "ALD AUTOMOTIVE PVT LTD",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 9,
                    "vehicleOwnershipSubType": "MAHINDRA & MAHINDRA",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 10,
                    "vehicleOwnershipSubType": "SMAS LEASING AUTO INDIA PVT LTD",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 11,
                    "vehicleOwnershipSubType": "WELECTRIC",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 12,
                    "vehicleOwnershipSubType": "AMPLUS POWER SUPPLY PRIVATE LIMITED",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 13,
                    "vehicleOwnershipSubType": "LOG9",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 14,
                    "vehicleOwnershipSubType": "VIODYUT PARIVAHAN LLP",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 17,
                    "vehicleOwnershipSubType": "GENSOL EV LEASE PVT. LTD",
                    "vehicleFinanceOptions": []
                }
            ]
        },
        {
            "vehicleOwnershipId": 3,
            "vehicleOwnershipType": "dco",
            "vehicleOwnershipSubtypes": [
                {
                    "vehicleOwnershipSubTypeId": 15,
                    "vehicleOwnershipSubType": "FINANCED BY MOEVING",
                    "vehicleFinanceOptions": []
                },
                {
                    "vehicleOwnershipSubTypeId": 16,
                    "vehicleOwnershipSubType": "EXTERNALLY FUNDED",
                    "vehicleFinanceOptions": []
                }
            ]
        }
    ]
    for ownership_type in master_list:
        if ownership_type["vehicleOwnershipId"] == ownership_id:
            vehicle_ownership = ownership_type["vehicleOwnershipType"]
            if ownership_id == 1 and ownership_subtype_id == 2:
                vehicle_finance_options = ownership_type["vehicleOwnershipSubtypes"][1]["vehicleFinanceOptions"]
                vehicle_ownership_subtype = "loan"
                for finance_option in vehicle_finance_options:
                    finance_option = dict(finance_option)
                    if finance_option["financeProviderId"] == finance_provider_id:
                        finance_provider = finance_option["financeProviderName"]

            else:
                for ownership_subtype in ownership_type["vehicleOwnershipSubtypes"]:
                    if ownership_subtype["vehicleOwnershipSubTypeId"] == ownership_subtype_id:
                        vehicle_ownership_subtype = ownership_type["vehicleOwnershipType"]
                        vehicle_lease_provider = ownership_subtype["vehicleOwnershipSubType"]

    return {
        "vehicleOwnership": vehicle_ownership,
        "vehicleOwnershipSubtype": vehicle_ownership_subtype,
        "financeProvider": finance_provider,
        "vehicleLeaseProvider": vehicle_lease_provider
    }
