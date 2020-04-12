def estimator(data_in):
        data = data_in
        infectionsByRequestedTime_Impact=''
        infectionsByRequestedTime_severeImpact=''

        final = {
        "data" : data,
        "impact" : {
            "currentlyInfected": data["reportedCases"] *10, 
            "infectionsByRequestedTime": infectionsByRequestedTime_Impact,

        },
        "severeImpact" : {
            "currentlyInfected" : data_in["reportedCases"] *50,
            "infectionsByRequestedTime": infectionsByRequestedTime_severeImpact,
        }
    }

        def infectionsByRequestedTime(data_input=data):
            if data["periodType"] == 'days':
                time = data["timeToElapse"] //3
                infectionsByRequestedTime_Impact = (final["impact"]["currentlyInfected"]) * (2**time)
                infectionsByRequestedTime_severeImpact  = (final["severeImpact"]["currentlyInfected"]) * (2**time)
            
            elif data["periodType"] == 'weeks':
                time = (data["timeToElapse"] *7) //3
                infectionsByRequestedTime_Impact = (final["impact"]["currentlyInfected"]) * (2**time)
                infectionsByRequestedTime_severeImpact  = (final["severeImpact"]["currentlyInfected"]) * (2**time)
            
            else:
                time = (data["timeToElapse"] *30) //3
                infectionsByRequestedTime_Impact = (final["impact"]["currentlyInfected"]) * (2**time)
                infectionsByRequestedTime_severeImpact  = (final["severeImpact"]["currentlyInfected"]) * (2**time)

            return infectionsByRequestedTime_Impact, infectionsByRequestedTime_severeImpact


        #challenge 2

        final["impact"]["infectionsByRequestedTime"] ,final["severeImpact"]["infectionsByRequestedTime"]= infectionsByRequestedTime()
        final["impact"]["severeCasesByRequestedTime"] = int(0.15 * (final["impact"]["infectionsByRequestedTime"]))
        final["severeImpact"]["severeCasesByRequestedTime"] = int(0.15 * (final["severeImpact"]["infectionsByRequestedTime"]))
        final["impact"]["hospitalBedsByRequestedTime"] = int((0.35 * (data["totalHospitalBeds"])) -  final["impact"]["severeCasesByRequestedTime"]) 
        final["severeImpact"]["hospitalBedsByRequestedTime"] = int((0.35 * (data["totalHospitalBeds"])) - final["severeImpact"]["severeCasesByRequestedTime"])

        #challenge 3
        final["impact"]["casesForICUByRequestedTime"] =  int((final["impact"]["infectionsByRequestedTime"]) * 0.05)
        final["impact"]["casesForVentilatorsByRequestedTime"] = int((final["impact"]["infectionsByRequestedTime"]) * 0.02)
        final["severeImpact"]["casesForICUByRequestedTime"] =  int((final["severeImpact"]["infectionsByRequestedTime"]) * 0.05)
        final["severeImpact"]["casesForVentilatorsByRequestedTime"] = int((final["severeImpact"]["infectionsByRequestedTime"]) * 0.02)

        def moneyLost(data_input=data):
            if data["periodType"] == 'days':
                time = data["timeToElapse"]
                moneyLostByRequestedTime_Impact = (data["region"]["avgDailyIncomePopulation"])* (data["region"]["avgDailyIncomeInUSD"]) *(final["impact"]["infectionsByRequestedTime"]) / time
                moneyLostByRequestedTime_severeImpact  = (data["region"]["avgDailyIncomePopulation"])* (data["region"]["avgDailyIncomeInUSD"]) *(final["severeImpact"]["infectionsByRequestedTime"]) / time
            
            elif data["periodType"] == 'weeks':
                time = (data["timeToElapse"] *7) 
                moneyLostByRequestedTime_Impact = (data["region"]["avgDailyIncomePopulation"])* (data["region"]["avgDailyIncomeInUSD"]) *(final["impact"]["infectionsByRequestedTime"]) / time
                moneyLostByRequestedTime_severeImpact  = (data["region"]["avgDailyIncomePopulation"])* (data["region"]["avgDailyIncomeInUSD"]) *(final["severeImpact"]["infectionsByRequestedTime"]) / time
            
            else:
                time = (data["timeToElapse"] *30)
                moneyLostByRequestedTime_Impact = (data["region"]["avgDailyIncomePopulation"])* (data["region"]["avgDailyIncomeInUSD"]) *(final["impact"]["infectionsByRequestedTime"]) / time
                moneyLostByRequestedTime_severeImpact  = (data["region"]["avgDailyIncomePopulation"])* (data["region"]["avgDailyIncomeInUSD"]) *(final["severeImpact"]["infectionsByRequestedTime"]) / time

            return int(moneyLostByRequestedTime_Impact) , int(moneyLostByRequestedTime_severeImpact)

        
        final["impact"]["dollarsInFlight"], final["severeImpact"]["dollarsInFlight"] = moneyLost()





        return final
