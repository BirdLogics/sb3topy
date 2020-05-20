"""
Generated with sb3topy
"""
import asyncio
import math            
import random

from engine import SpriteBase

class Stage(SpriteBase):
    pass


class skyautoroute(SpriteBase):
    async def on_newAutoroute_1(self):
        for _ in range(self.variable['route_grid_size']):
            self.lists['_routeGrid'].append("0")
        for _ in range(32):
            self.lists['_routeBuf'].append("0")

    async def on_AutorouteautoRoute_2(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cptScreen'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3]
        self.lists['Params'].append(self.variable['cpt'])
        event_broadcastandwait
        self.variable['cptWidth'] = self.lists['SkyCompact._RawBuff'][self.variable['Return value']]
        procedures_call
        procedures_call
        self.variable['startX'] = self.variable['blkX']
        self.variable['initStaX'] = self.variable['initX']
        procedures_call
        self.variable['startY'] = self.variable['blkY']
        self.variable['initStaY'] = self.variable['initY']
        procedures_call
        self.variable['destX'] = self.variable['blkX']
        self.variable['initDestX'] = self.variable['initX']
        procedures_call
        self.variable['destY'] = self.variable['blkY']
        self.variable['initDestY'] = self.variable['initY']
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 53])
        event_broadcastandwait
        self.variable['routeDest'] = self.variable['Return value']
        self.variable['i'] = "0"
        for _ in range(32):
            self.lists['SkyCompact._RawBuff'][self.variable['routeDest'] + self.variable['i']] = "0"
            self.variable['i'] += 1
        if self.variable['startX'] == self.variable['destX'] and self.variable['startY'] == self.variable['destY']:
            self.variable['Return value'] = "2"
            control_stop
        if not self.lists['_routeGrid'][self.variable['destY'] + 1 * 42 + self.variable['destX'] + 2] == "0":
            self.lists['Params'].append(self.variable['cpt'])
            self.lists['Params'].append("3")
            event_broadcastandwait
            if self.variable['Return value'] == "true" and self.variable['cptScreen'] == "12" and self.variable['destX'] == "2" and self.variable['destY'] == "14":
                self.lists['_routeGrid'][self.variable['destY'] + 1 * 42 + self.variable['destX'] + 2] = "0"
            else:
                self.variable['Return value'] = "1"
                control_stop
        procedures_call
        if self.variable['Return value'] == "false":
            self.variable['Return value'] = "1"
            control_stop
        procedures_call
        self.variable['routeData'] = self.variable['Return value']
        procedures_call
        self.variable['routeData'] = self.variable['Return value']
        self.variable['cnt'] = "0"
        while True:
            self.lists['SkyCompact._RawBuff'][self.variable['routeDest'] + self.variable['cnt']] = self.lists['_routeBuf'][self.variable['routeData'] + self.variable['cnt']]
            self.lists['SkyCompact._RawBuff'][self.variable['routeDest'] + self.variable['cnt'] + 1] = self.lists['_routeBuf'][self.variable['routeData'] + self.variable['cnt'] + 1]
            self.variable['cnt'] += 2
            if self.lists['_routeBuf'][self.variable['routeData'] + self.variable['cnt'] - 2] == "0":
                self.variable['Return value'] = "0"
                control_stop

    async def on_Scratchreset_3(self):
        self.lists['_routeGrid'] = []
        self.lists['_routeBuf'] = []
        self.lists['_routeDirections'] = []
        self.lists['_logicCommands'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist

    async def on_Scratchinitialise_4(self):
        self.variable['route_grid_width'] = "42"
        self.variable['route_grid_height'] = "26"
        self.variable['route_grid_size'] = self.variable['route_grid_width'] * self.variable['route_grid_height']
        self.lists['_routeDirections'].append("-1")
        self.lists['_routeDirections'].append("1")
        self.lists['_routeDirections'].append("-42")
        self.lists['_routeDirections'].append("42")
        self.lists['_logicCommands'].append("3")
        self.lists['_logicCommands'].append("2")
        self.lists['_logicCommands'].append("1")
        self.lists['_logicCommands'].append("0")

    async def on_deleteAutoroute_5(self):
        self.lists['_routeGrid'] = []
        self.lists['_routeBuf'] = []


class skycompact(SpriteBase):
    async def on_newSkyCompact_6(self):
        pen_setPenColorToColor
        pen_setPenSizeTo
        pen_penUp
        self.variable['x'] = "-196"
        self.xpos = self.variable['x']
        event_broadcastandwait
        self.variable['srcBuf'] = self.variable['Return value']
        self.variable['srcPos'] = "0"
        procedures_call
        self.variable['_numDataLists'] = self.variable['Return value']
        self.variable['offset'] = "1"
        for _ in range(self.variable['_numDataLists']):
            procedures_call
            self.lists['_dataListLen'].append(self.variable['Return value'])
            self.lists['SkyCompact._DataOffsets'].append(self.variable['offset'])
            self.variable['offset'] += self.variable['Return value']
        self.variable['xStep'] = 170 / 148603
        procedures_call
        self.variable['rawSize'] = self.variable['Return value']
        self.variable['rawPos'] = "1"
        procedures_call
        self.variable['srcSize'] = self.variable['Return value']
        self.variable['diskPos'] = self.variable['srcPos'] + self.variable['srcSize']
        procedures_call
        self.variable['lcnt'] = "1"
        for _ in range(self.variable['_numDataLists']):
            for _ in range(self.lists['_dataListLen'][self.variable['lcnt']]):
                procedures_call
                self.lists['_cptSizes'].append(self.variable['Return value'])
                if not self.variable['Return value'] == "0":
                    procedures_call
                    self.lists['_cptTypes'].append(self.variable['Return value'])
                    self.lists['SkyCompact._Compacts'].append(self.variable['rawPos'])
                    for _ in range(self.lists['_cptSizes'][len(self.lists['_cptSizes'])]):
                        self.lists['SkyCompact._RawBuff'].append(data_itemnumoflist - 1 * 16 + data_itemnumoflist - 1 + data_itemnumoflist - 1 * 16 + data_itemnumoflist - 1 * 256)
                        self.variable['srcPos'] += 2
                        self.variable['x'] += self.variable['xStep']
                        if operator_mathop == self.xpos + 2:
                            pen_penUp
                            self.xpos += 2
                            self.ypos = -114
                            pen_penDown
                            self.ypos += -40
                    self.variable['rawPos'] += self.lists['_cptSizes'][len(self.lists['_cptSizes'])]
                else:
                    self.lists['SkyCompact._Compacts'].append("0")
            self.variable['lcnt'] += 1
        self.variable['srcPos'] = self.variable['diskPos']
        procedures_call
        self.variable['numDlincs'] = self.variable['Return value']
        for _ in range(self.variable['numDlincs']):
            procedures_call
            self.variable['dlincId'] = self.variable['Return value']
            procedures_call
            self.variable['destId'] = self.variable['Return value']
            procedures_call
            self.variable['temp'] = self.lists['SkyCompact._Compacts'][self.variable['Return value']]
            procedures_call
            self.lists['SkyCompact._Compacts'][self.variable['Return value']] = self.variable['temp']
        procedures_call
        self.variable['_numSaveIds'] = self.variable['Return value']
        for _ in range(self.variable['_numSaveIds']):
            procedures_call
            self.lists['SkyCompact._SaveIds'].append(self.variable['Return value'])
        self.variable['_resetDataPos'] = self.variable['srcPos']
        procedures_call

    async def on_SkyCompactcptIsId_7(self):
        self.variable['id'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append(self.variable['id'])
        event_broadcastandwait
        self.variable['Return value'] = self.variable['cpt'] == self.variable['Return value']

    async def on_SkyCompactfetchCpt_8(self):
        self.variable['cptId'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if self.variable['cptId'] == "65535":
            self.variable['Return value'] = "0"
            self.lists['Params'].append("3")
            event_broadcastandwait
            if self.variable['Debug?'] == "true":
                sensing_askandwait
            control_stop
        self.variable['Return value'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['cptId'] / 4096 + 1] + self.variable['cptId'] % 4096]

    async def on_SkyCompactfetchCptInfo_9(self):
        self.variable['cptId'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['temp'] = self.lists['SkyCompact._DataOffsets'][self.variable['cptId'] / 4096 + 1] + self.variable['cptId'] % 4096
        self.variable['elems'] = self.lists['_cptSizes'][self.variable['temp']]
        self.variable['Return value'] = self.lists['SkyCompact._Compacts'][self.variable['temp']]

    async def on_SkyCompactnameForType_10(self):
        self.lists['Params'].append("SkyCompact.nameForType")
        event_broadcastandwait

    async def on_SkyCompactgetSub_11(self):
        self.variable['mode'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 27 + self.variable['mode'] / 2]
        if self.variable['Debug?'] == "true":
            if self.variable['mode'] < "0" or self.variable['mode'] > "14" or self.variable['mode'] % 2 == "1":
                self.lists['Params'].append("SkyCompact.getSub error")
                event_broadcastandwait

    async def on_SkyCompactsetSub_12(self):
        self.variable['value'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['mode'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 27 + self.variable['mode'] / 2] = self.variable['value']
        if self.variable['Debug?'] == "true":
            if self.variable['mode'] < "0" or self.variable['mode'] > "14" or self.variable['mode'] % 2 == "1":
                self.lists['Params'].append("SkyCompact.setSub error")
                event_broadcastandwait

    async def on_SkyCompactgetGrafixPtr_13(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 23]
        self.variable['gfxBase'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        if self.variable['gfxBase'] == "0":
            self.variable['Return value'] = "0"
        else:
            self.variable['Return value'] = self.variable['gfxBase'] + self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 24]

    async def on_SkyCompactgetMegaSet_14(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = self.variable['cpt'] + 55 + self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] / 144 * 14
        if self.variable['Debug?'] == "true":
            if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] < "0" or self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] > "432" or self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] % 144 > "0":
                self.lists['Params'].append("SkyCompact.getMegaSet error")
                event_broadcastandwait

    async def on_SkyCompactgetTurnTable_15(self):
        self.variable['dir'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['m'] = self.variable['cpt'] + 55 + self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] / 144 * 14
        if self.variable['Debug?'] == "true":
            if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] < "0" or self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] > "432" or self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] % 144 > "0":
                self.lists['Params'].append("SkyCompact.getMegaSet error")
                event_broadcastandwait
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['m'] + 13]
        self.variable['turnTable'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        self.variable['Return value'] = self.variable['turnTable'] + self.variable['dir'] * 5
        if self.variable['Debug?'] == "true":
            if self.variable['dir'] < "0" or self.variable['dir'] > "4":
                self.lists['Params'].append("SkyCompact.getTurnTable: Error")
                event_broadcastandwait

    async def on_SkyCompactgetCompactElem_16(self):
        self.variable['off'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if self.variable['off'] < "114":
            self.variable['Return value'] = self.variable['cpt'] + self.lists['compactOffsets'][self.variable['off'] + 1] / 2
        else:
            self.variable['off'] += -114
            if self.variable['off'] < "44":
                self.variable['Return value'] = self.variable['cpt'] + 55 + self.lists['megaSetOffsets'][self.variable['off'] + 1] / 2
            else:
                self.variable['off'] += -44
                if self.variable['off'] < "100":
                    self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 55 + 13]
                    self.variable['Return value'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + self.lists['turnTableOffsets'][self.variable['off'] + 1] / 2
                else:
                    self.variable['off'] += -100
                    if self.variable['off'] < "44":
                        self.variable['Return value'] = self.variable['cpt'] + 69 + self.lists['megaSetOffsets'][self.variable['off'] + 1] / 2
                    else:
                        self.variable['off'] += -44
                        if self.variable['off'] < "100":
                            self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 69 + 13]
                            self.variable['Return value'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + self.lists['turnTableOffsets'][self.variable['off'] + 1] / 2
                        else:
                            self.variable['off'] += -100
                            if self.variable['off'] < "44":
                                self.variable['Return value'] = self.variable['cpt'] + 83 + self.lists['megaSetOffsets'][self.variable['off'] + 1] / 2
                            else:
                                self.variable['off'] += -44
                                if self.variable['off'] < "100":
                                    self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 83 + 13]
                                    self.variable['Return value'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + self.lists['turnTableOffsets'][self.variable['off'] + 1] / 2
                                else:
                                    self.variable['off'] += -100
                                    if self.variable['off'] < "44":
                                        self.variable['Return value'] = self.variable['cpt'] + 97 + self.lists['megaSetOffsets'][self.variable['off'] + 1] / 2
                                    else:
                                        self.variable['off'] += -44
                                        if self.variable['off'] < "100":
                                            self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 97 + 13]
                                            self.variable['Return value'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + self.lists['turnTableOffsets'][self.variable['off'] + 1] / 2
                                        else:
                                            self.variable['off'] += -100

    async def on_SkyCompactcreateResetData_17(self):
        procedures_call

    async def on_SkyCompactfindCptId_18(self):
        self.lists['Params'].append("SkyCompact.findCptId")
        event_broadcastandwait

    async def on_SkyCompactgiveNumDataLists_19(self):
        self.lists['Params'].append("SkyCompact.giveNumDataLists")
        event_broadcastandwait

    async def on_SkyCompactgiveDataListLen_20(self):
        self.lists['Params'].append("SkyCompact.giveDataListLen")
        event_broadcastandwait

    async def on_Scratchinitialise_21(self):
        event_broadcastandwait
        self.variable['a'] = self.variable['Return value']
        event_broadcastandwait
        self.variable['b'] = self.variable['Return value']
        event_broadcastandwait
        procedures_call

    async def on_Scratchreset_22(self):
        self.lists['_dataListLen'] = []
        self.lists['_cptTypes'] = []
        self.lists['_cptSizes'] = []
        self.lists['SkyCompact._Compacts'] = []
        self.lists['SkyCompact._RawBuff'] = []
        self.lists['SkyCompact._SaveIds'] = []
        self.lists['compactOffsets'] = []
        self.lists['megaSetOffsets'] = []
        self.lists['turnTableOffsets'] = []
        self.lists['SkyCompact._DataOffsets'] = []
        self.lists['SaveGameData'] = []
        self.variable['srcBuf'] = ""
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showvariable
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidevariable


class skycontrol(SpriteBase):
    async def on_newControl_23(self):
        pass

    async def on_newConResource_24(self):
        self.lists['Params'].append("new ConResource")
        event_broadcastandwait

    async def on_ConResourceisMouseOver_25(self):
        self.lists['Params'].append("ConResource.isMouseOver")
        event_broadcastandwait

    async def on_ConResourcedrawToScreen_26(self):
        self.lists['Params'].append("ConResource.drawToScreen")
        event_broadcastandwait

    async def on_newTextResource_27(self):
        self.lists['Params'].append("new TextResource")
        event_broadcastandwait

    async def on_TextResourceflushForRedraw_28(self):
        self.lists['Params'].append("TextResource.flushForRedraw")
        event_broadcastandwait

    async def on_TextResourcedrawToScreen_29(self):
        self.lists['Params'].append("TextResource.drawToScreen")
        event_broadcastandwait

    async def on_newControlStatus_30(self):
        self.lists['Params'].append("new ControlStatus")
        event_broadcastandwait

    async def on_ControlStatussetToText_31(self):
        self.lists['Params'].append("ControlStatus.setToText")
        event_broadcastandwait

    async def on_ControlStatusdrawToScreen_32(self):
        self.lists['Params'].append("ControlStatus.drawToScreen")
        event_broadcastandwait

    async def on_ControlcreateResource_33(self):
        self.lists['Params'].append("Control.createResource")
        event_broadcastandwait

    async def on_ControlremovePanel_34(self):
        self.lists['Params'].append("Control.removePanel")
        event_broadcastandwait

    async def on_ControlinitPanel_35(self):
        self.lists['Params'].append("Control.initPanel")
        event_broadcastandwait

    async def on_ControldrawMainPanel_36(self):
        self.lists['Params'].append("Control.drawMainPanel")
        event_broadcastandwait

    async def on_ControldoLoadSavePanel_37(self):
        self.lists['Params'].append("Control.doLoadSavePanel")
        event_broadcastandwait

    async def on_ControldoControlPanel_38(self):
        self.lists['Params'].append("Control.doControlPanel")
        event_broadcastandwait

    async def on_ControlloadDescriptions_39(self):
        self.lists['Params'].append("Control.loadDescriptions")
        event_broadcastandwait

    async def on_ControlloadSaveAllowed_40(self):
        self.lists['Params'].append("Control.loadSaveAllowed")
        event_broadcastandwait

    async def on_ControlsaveDescriptions_41(self):
        self.lists['Params'].append("Control.saveDescriptions")
        event_broadcastandwait

    async def on_ControldoAutoSave_42(self):
        self.lists['Params'].append("Control.doAutoSave")
        event_broadcastandwait

    async def on_ControlsaveGameToFile_43(self):
        self.lists['Params'].append("Control.saveGameToFile")
        event_broadcastandwait
        procedures_call

    async def on_ControlquickXRestore_44(self):
        self.lists['Params'].append("Control.quickXRestore")
        event_broadcastandwait
        sensing_askandwait
        self.xpos = 0
        self.ypos = -144
        self.switch_costume('loading')
        looks_gotofrontback
        self.visible = 1
        self.variable['i'] = sensing_of
        for _ in range(len(self.lists['SaveGameData']) - self.variable['i'] + 1):
            self.lists['SaveGameData'].pop(self.variable['i'])
        self.variable['j'] = "0"
        self.variable['i'] = "1"
        while not self.variable['j'] == operator_length / 2:
            procedures_call
            self.variable['j'] += 2
            for _ in range(self.variable['Return value']):
                self.lists['SaveGameData'].append(self.lists['SaveGameData'][self.variable['i']])
                self.variable['i'] += 1
            if self.variable['j'] < operator_length / 2:
                procedures_call
                self.variable['j'] += 2
                self.variable['diffCtr'] = self.variable['Return value']
                for _ in range(self.variable['diffCtr']):
                    procedures_call
                    self.variable['j'] += 2
                    self.lists['SaveGameData'].append(self.variable['Return value'])
                    self.variable['i'] += 1
        procedures_call
        self.variable['i'] = sensing_of
        for _ in range(len(self.lists['SaveGameData']) - self.variable['i'] + 1):
            self.lists['SaveGameData'].pop(self.variable['i'])
        self.variable['_SystemVars.pastIntro'] = "true"
        self.visible = 0

    async def on_ControlrestartGame_45(self):
        procedures_call
        self.lists['Params'].append(self.variable['_savedMouse'])
        self.lists['Params'].append("0")
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.variable['_SystemVars.pastIntro'] = "true"

    async def on_Controldelay_46(self):
        self.lists['Params'].append("Control.delay")
        event_broadcastandwait

    async def on_ControlshowGameQuitMsg_47(self):
        self.lists['Params'].append("Control.showGameQuitMsg")
        event_broadcastandwait

    async def on_Scratchreset_48(self):
        self.lists['reloadList'] = []
        self.lists['SaveCode'] = []
        self.lists['compressed'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist
        self.variable['destBuf'] = ""
        self.visible = 0


class skydisk(SpriteBase):
    async def on_newDisk_49(self):
        self.lists['_buildList'] = []
        self.lists['SkyCompact._LoadedFilesList'] = []
        for _ in range(60):
            self.lists['_buildList'].append("0")
            self.lists['SkyCompact._LoadedFilesList'].append("0")
        self.lists['fileNumbers'] = []
        procedures_call
        self.variable['_dinnerTableEntries'] = "1445"
        self.variable['index'] = "0"
        for _ in range(self.variable['_dinnerTableEntries']):
            procedures_call
            self.lists['fileNumbers'].append(self.variable['Return value'])
            self.variable['index'] += 2

    async def on_DiskfileExists_50(self):
        self.variable['fileNr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        self.variable['Return value'] = self.variable['Return value'] > "0"

    async def on_DiskloadFile_51(self):
        self.variable['fileNr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait
        if self.variable['Debug?'] == "true":
            if self.variable['Return value'] == "":
                self.lists['Params'].append("File " + self.variable['fileNr'] + " has no data")
                event_broadcastandwait

    async def on_DiskloadScriptFile_52(self):
        self.variable['fileNr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append(self.variable['fileNr'])
        event_broadcastandwait

    async def on_DiskfnCacheChip_53(self):
        self.variable['fList'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cnt'] = "0"
        while not self.lists['_buildList'][self.variable['cnt'] + 1] == "0":
            self.variable['cnt'] += 1
        self.variable['fCnt'] = "0"
        while True:
            self.lists['_buildList'][self.variable['cnt'] + self.variable['fCnt'] + 1] = self.lists['SkyCompact._RawBuff'][self.variable['fList'] + self.variable['fCnt']] % 32768
            self.variable['fCnt'] += 1
            if self.lists['SkyCompact._RawBuff'][self.variable['fList'] + self.variable['fCnt'] - 1] == "0":
                event_broadcastandwait
                control_stop

    async def on_DiskfnCacheFast_54(self):
        self.variable['fList'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if not self.variable['fList'] == "0":
            self.variable['cnt'] = "0"
            while True:
                self.lists['_buildList'][self.variable['cnt'] + 1] = self.lists['SkyCompact._RawBuff'][self.variable['fList'] + self.variable['cnt']] % 32768
                self.variable['cnt'] += 1
                if self.lists['SkyCompact._RawBuff'][self.variable['fList'] + self.variable['cnt'] - 1] == "0":
                    control_stop

    async def on_DiskfnCacheFiles_55(self):
        self.variable['targCnt'] = "0"
        self.variable['lCnt'] = "0"
        while not self.lists['SkyCompact._LoadedFilesList'][self.variable['lCnt'] + 1] == "0":
            self.variable['bCnt'] = "0"
            self.variable['found'] = "false"
            while not self.lists['_buildList'][self.variable['bCnt'] + 1] == "0" or self.variable['found'] == "true":
                if self.lists['_buildList'][self.variable['bCnt'] + 1] % 32768 == self.lists['SkyCompact._LoadedFilesList'][self.variable['lCnt'] + 1]:
                    self.variable['found'] = "true"
                else:
                    self.variable['bCnt'] += 1
            if self.variable['found'] == "true":
                self.lists['SkyCompact._LoadedFilesList'][self.variable['targCnt'] + 1] = self.lists['SkyCompact._LoadedFilesList'][self.variable['lCnt'] + 1]
                self.variable['targCnt'] += 1
            else:
                self.lists['SkyEngine._ItemList'][self.lists['SkyCompact._LoadedFilesList'][self.variable['lCnt'] + 1] % 2048 + 1] = "0"
            self.variable['lCnt'] += 1
        self.lists['SkyCompact._LoadedFilesList'][self.variable['targCnt'] + 1] = "0"
        self.variable['bCnt'] = "0"
        while not self.lists['_buildList'][self.variable['bCnt'] + 1] == "0":
            if self.lists['_buildList'][self.variable['bCnt'] + 1] % 2048 == "2047":
                self.variable['bCnt'] += 1
            else:
                self.variable['lCnt'] = "0"
                self.variable['found'] = "false"
                while not self.lists['SkyCompact._LoadedFilesList'][self.variable['lCnt'] + 1] == "0" or self.variable['found'] == "true":
                    if self.lists['SkyCompact._LoadedFilesList'][self.variable['lCnt'] + 1] == self.lists['_buildList'][self.variable['bCnt'] + 1] % 32768:
                        self.variable['found'] = "true"
                    self.variable['lCnt'] += 1
                if self.variable['found'] == "true":
                    self.variable['bCnt'] += 1
                else:
                    self.lists['SkyCompact._LoadedFilesList'][self.variable['targCnt'] + 1] = self.lists['_buildList'][self.variable['bCnt'] + 1] % 32768
                    self.variable['targCnt'] += 1
                    self.lists['SkyCompact._LoadedFilesList'][self.variable['targCnt'] + 1] = "0"
                    self.lists['Params'].append(self.lists['_buildList'][self.variable['bCnt'] + 1] % 32768)
                    event_broadcastandwait
                    self.lists['SkyEngine._ItemList'][self.lists['_buildList'][self.variable['bCnt'] + 1] % 2048 + 1] = self.variable['Return value']
                    self.variable['bCnt'] += 1
        self.lists['_buildList'][1] = "0"

    async def on_DiskrefreshFilesList_56(self):
        self.variable['cnt'] = "1"
        while not self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] == "0":
            self.lists['SkyEngine._ItemList'][self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] % 2048 + 1] = "0"
            self.variable['cnt'] += 1
        self.variable['cnt'] = "1"
        while not self.lists['Generic list'][self.variable['cnt']] == "0":
            self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] = self.lists['Generic list'][self.variable['cnt']]
            self.lists['Params'].append(self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] % 32768)
            event_broadcastandwait
            self.lists['SkyEngine._ItemList'][self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] % 2048 + 1] = self.variable['Return value']
            self.variable['cnt'] += 1
        self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] = "0"

    async def on_DiskfnMiniLoad_57(self):
        self.variable['fileNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cnt'] = "1"
        while not self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] == "0":
            if self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] == self.variable['fileNum']:
                control_stop
            self.variable['cnt'] += 1
        self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt']] = self.variable['fileNum'] % 32768
        self.lists['SkyCompact._LoadedFilesList'][self.variable['cnt'] + 1] = "0"
        self.lists['Params'].append(self.variable['fileNum'])
        event_broadcastandwait
        self.lists['SkyEngine._ItemList'][self.lists['SkyCompact._LoadedFilesList'][self.variable['fileNum']] % 2048 + 1] = self.variable['Return value']

    async def on_DiskdumpFile_58(self):
        self.lists['Params'].append("Disk.dumpFile")
        event_broadcastandwait

    async def on_DiskdetermineGameVersion_59(self):
        self.variable['Return value'] = "348"

    async def on_Scratchreset_60(self):
        self.lists['_buildList'] = []
        self.lists['SkyCompact._LoadedFilesList'] = []
        self.lists['fileNumbers'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist

    async def on_deleteDisk_61(self):
        procedures_call

    async def on_DiskfnFlushBuffers_62(self):
        procedures_call

    async def on_diskloadSprite_63(self):
        self.variable['fileNr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append(self.variable['fileNr'])
        event_broadcastandwait
        if not operator_length == "44":
            if self.variable['Debug?'] == "true":
                self.lists['Params'].append("File " + self.variable['fileNr'] + " is not a sprite")
                event_broadcastandwait
            self.variable['Return value'] = "0"
        else:
            self.variable['fileNr'] = self.variable['fileNr'] % 2047
            self.variable['j'] = self.variable['fileNr'] * 11 + 1
            self.variable['i'] = "1"
            for _ in range(11):
                self.lists['Sprites.data'][self.variable['j']] = data_itemnumoflist - 1 * 16 + data_itemnumoflist - 1 + data_itemnumoflist - 1 * 16 + data_itemnumoflist - 1 * 256
                self.variable['i'] += 4
                self.variable['j'] += 1
            self.variable['Return value'] = self.variable['fileNr'] * 11 + 1
            if self.lists['Sprites.data'][self.variable['Return value'] + 8] > "32767":
                self.lists['Sprites.data'][self.variable['Return value'] + 8] = self.lists['Sprites.data'][self.variable['Return value'] + 8] - 65536
            if self.lists['Sprites.data'][self.variable['Return value'] + 9] > "32767":
                self.lists['Sprites.data'][self.variable['Return value'] + 9] = self.lists['Sprites.data'][self.variable['Return value'] + 9] - 65536


class skygrid(SpriteBase):
    async def on_newGrid_64(self):
        self.variable['cnt'] = "1"
        for _ in range(70):
            self.lists['_gameGrids'][self.variable['cnt']] = "0"
            self.variable['cnt'] += 1

    async def on_GridloadGrids_65(self):
        self.lists['Grid._GameGrids'] = []
        event_broadcastandwait
        self.variable['hex'] = self.variable['Return value']
        self.variable['i'] = "1"
        self.variable['cnt'] = "1"
        for _ in range(70):
            self.lists['_gameGrids'][self.variable['cnt']] = self.variable['i']
            for _ in range(120):
                procedures_call
                self.lists['Grid._GameGrids'].append(self.variable['Return value'])
                self.variable['i'] += 1
            self.variable['cnt'] += 1
        self.variable['hex'] = ""
        if not self.lists['Logic._ScriptVariables'][sensing_of] == "0":
            self.lists['Params'].append("12459")
            event_broadcastandwait
            self.lists['Params'].append("256")
            self.lists['Params'].append("280")
            self.lists['Params'].append("1")
            self.lists['Params'].append(self.variable['Return value'])
            event_broadcastandwait

    async def on_GridremoveObjectFromWalk_66(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        if self.variable['Return value'] == "true":
            procedures_call

    async def on_GridobjectToWalk_67(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        if self.variable['Return value'] == "true":
            procedures_call

    async def on_GridplotGrid_68(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['width'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['y'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['x'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        if self.variable['Return value'] == "true":
            procedures_call

    async def on_GridremoveGrid_69(self):
        self.variable['cpt'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['width'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['y'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['x'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        if self.variable['Return value'] == "true":
            procedures_call

    async def on_GridgiveGrid_70(self):
        self.variable['pScreen'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if not self.lists['_gridConvertTable'][self.variable['pScreen'] + 1] < "0" and self.lists['_gridConvertTable'][self.variable['pScreen'] + 1] < "70":
            self.variable['Return value'] = self.lists['_gameGrids'][self.lists['_gridConvertTable'][self.variable['pScreen'] + 1] + 1]
        else:
            self.variable['Return value'] = "0"

    async def on_Scratchreset_71(self):
        self.lists['_gameGrids'] = []
        self.lists['Grid._GameGrids'] = []
        self.lists['_gridConvertTable'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist

    async def on_Scratchinitialise_72(self):
        procedures_call
        for _ in range(70):
            self.lists['_gameGrids'].append("0")
        event_broadcastandwait
        self.variable['hex'] = self.variable['Return value']
        self.variable['i'] = "0"
        for _ in range(97):
            procedures_call
            if self.variable['Return value'] > "127":
                self.variable['Return value'] += -256
            self.lists['_gridConvertTable'].append(self.variable['Return value'])
            self.variable['i'] += 1
        self.variable['hex'] = ""


class skylogic(SpriteBase):
    async def on_newLogic_73(self):
        event_broadcastandwait
        event_broadcastandwait
        procedures_call
        procedures_call
        procedures_call
        procedures_call
        self.variable['_stackPtr'] = "0"
        self.variable['_currentSection'] = "255"
        event_broadcastandwait

    async def on_LogicinitScreen_74(self):
        procedures_call
        self.lists['Params'].append("2")
        event_broadcastandwait
        self.variable['_SystemVars.currentMusic'] = "2"

    async def on_Logicengine_75(self):
        self.variable['checkProtection?'] = "true"
        while not self.variable['checkProtection?'] == "false":
            self.variable['temp'] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.LOGIC_LIST_NO']]
            self.variable['logicList'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
            self.variable['id'] = self.lists['SkyCompact._RawBuff'][self.variable['logicList']]
            self.variable['logicList'] += 1
            while not self.variable['id'] == "0":
                if self.variable['id'] == "65535":
                    self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['logicList']]
                    self.variable['logicList'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
                else:
                    self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.CUR_ID']] = self.variable['id']
                    self.variable['_compact'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['id'] / 4096 + 1] + self.variable['id'] % 4096]
                    if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] % 128 > "63":
                        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] % 256 > "127":
                            self.lists['Params'].append(self.variable['_compact'])
                            event_broadcastandwait
                        if self.variable['Debug?'] == "true":
                            self.lists['Params'].append("PROCESSING COMPACT# " + self.variable['id'])
                            event_broadcastandwait
                            self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact']])
                            event_broadcastandwait
                        event_broadcastandwait
                        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] % 256 > "127":
                            self.lists['Params'].append(self.variable['_compact'])
                            event_broadcastandwait
                        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 2] = "0"
                self.variable['id'] = self.lists['SkyCompact._RawBuff'][self.variable['logicList']]
                self.variable['logicList'] += 1
            procedures_call
            self.variable['checkProtection?'] = self.variable['Return value']

    async def on_Logicnop_76(self):
        pass

    async def on_LogiclogicScript_77(self):
        while True:
            self.variable['_mode'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26]
            self.lists['Params'].append(self.variable['_compact'])
            self.lists['Params'].append(self.variable['_mode'])
            event_broadcastandwait
            self.variable['_scriptNo'] = self.variable['Return value']
            self.lists['Params'].append(self.variable['_compact'])
            self.lists['Params'].append(self.variable['_mode'] + 2)
            event_broadcastandwait
            self.variable['_offset'] = self.variable['Return value']
            procedures_call
            self.variable['_offset'] = self.variable['Return value']
            self.lists['Params'].append(self.variable['_compact'])
            self.lists['Params'].append(self.variable['_mode'] + 2)
            self.lists['Params'].append(self.variable['_offset'])
            event_broadcastandwait
            if self.variable['_offset'] == "0":
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] = self.variable['_mode'] - 4
            else:
                if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] == self.variable['_mode']:
                    control_stop

    async def on_LogicautoRoute_78(self):
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 19] = self.variable['Return value']
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append("1")
        event_broadcastandwait
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 19] == "2" and self.variable['Return value'] == "true" and self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] == "0" and self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 27] == "12577":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 19] = "0"
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 19] == "1":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 53]
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        event_broadcastandwait

    async def on_LogicarAnim_79(self):
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 6] % 8 == "0" or not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 7] % 8 == "0":
            procedures_call
            control_stop
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50] == "65535":
            procedures_call
            control_stop
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50] == "0":
            self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50]
            procedures_call
            if self.variable['Return value'] == "true":
                procedures_call
                control_stop
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50] = "0"
        self.variable['temp'] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.LOGIC_LIST_NO']]
        self.variable['_logicList'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        self.variable['id'] = self.lists['SkyCompact._RawBuff'][self.variable['_logicList']]
        self.variable['_logicList'] += 1
        while not self.variable['id'] == "0":
            if self.variable['id'] == "65535":
                self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_logicList']]
                self.variable['_logicList'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
            else:
                if not self.variable['id'] == self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.CUR_ID']] % 65536:
                    self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.HIT_ID']] = self.variable['id']
                    self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['id'] / 4096 + 1] + self.variable['id'] % 4096]
                    if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] % 64 > "31":
                        if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3] == self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 3]:
                            procedures_call
                            if self.variable['Return value'] == "true":
                                if not self.lists['SkyCompact._RawBuff'][self.variable['cpt']] == "3":
                                    self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50] = "65535"
                                    self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 50] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.CUR_ID']] % 65536
                                    self.lists['Params'].append(self.variable['_compact'])
                                    self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 2)
                                    self.lists['Params'].append("0")
                                    event_broadcastandwait
                                    self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
                                    event_broadcastandwait
                                    control_stop
                                procedures_call
                                control_stop
            self.variable['id'] = self.lists['SkyCompact._RawBuff'][self.variable['_logicList']]
            self.variable['_logicList'] += 1
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 42] == "0":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] = "4"
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 29] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 42]
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 30] = "0"
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 42] = "0"
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
            event_broadcastandwait
            control_stop
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 39] == "0":
            procedures_call
            control_stop
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 40] == self.lists['Logic._ScriptVariables'][self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 39] / 4 + 1]:
            procedures_call
            control_stop
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 2)
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        event_broadcastandwait

    async def on_LogicarTurn_80(self):
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 48]
        self.variable['turnData'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 8] = self.lists['SkyCompact._RawBuff'][self.variable['turnData']]
        self.variable['turnData'] += 1
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49] + 1
        if self.lists['SkyCompact._RawBuff'][self.variable['turnData']] == "0":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 47] = "0"
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "3"

    async def on_Logicalt_81(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 41])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 2)
        self.lists['Params'].append("0")
        event_broadcastandwait
        event_broadcastandwait

    async def on_Logicturn_82(self):
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 48]
        self.variable['turnData'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49]
        if not self.lists['SkyCompact._RawBuff'][self.variable['turnData']] == "0":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 8] = self.lists['SkyCompact._RawBuff'][self.variable['turnData']]
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49] + 1
            control_stop
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 47] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        event_broadcastandwait

    async def on_Logiccursor_83(self):
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait

    async def on_Logictalk_84(self):
        event_broadcastandwait
        if self.variable['Return value'] == "true":
            self.variable['i'] = "1"
            for _ in range(46):
                if self.lists['clickTable'][self.variable['i']] == self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.CUR_ID']]:
                    if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 45] > "0" and self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 45] < "65535":
                        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 45]
                        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
                        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "0"
                        self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8])
                        event_broadcastandwait
                    self.lists['Params'].append(self.variable['_compact'])
                    event_broadcastandwait
                    self.variable['graphixProg'] = self.variable['Return value']
                    if not self.variable['graphixProg'] == "0":
                        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 8] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 20]
                        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = "0"
                    self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
                    event_broadcastandwait
                    control_stop
                self.variable['i'] += 1
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.variable['graphixProg'] = self.variable['Return value']
        if not self.variable['graphixProg'] == "0":
            if not self.lists['SkyCompact._RawBuff'][self.variable['graphixProg']] == "0" and not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 46] == "3":
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 8] = self.lists['SkyCompact._RawBuff'][self.variable['graphixProg'] + 2] + self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 25]
                self.variable['graphixProg'] += 3
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] + 3
            else:
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 8] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 20]
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 46] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 46] - 1
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 46] == "0":
            if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 45] == "0":
                self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 45]
                self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
                self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "0"
                self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8])
                event_broadcastandwait
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
            event_broadcastandwait

    async def on_Logiclisten_85(self):
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 21]
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        if self.lists['SkyCompact._RawBuff'][self.variable['cpt']] == "9":
            control_stop
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        event_broadcastandwait

    async def on_Logicstopped_86(self):
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50]
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        if not self.variable['cpt'] == "0":
            procedures_call
            if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 22] == "0" and self.variable['Return value'] == "true":
                control_stop
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] - 2)
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50] = "65535"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        event_broadcastandwait

    async def on_Logicchoose_87(self):
        if self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.THE_CHOSEN_ONE']] == "0":
            control_stop
        procedures_call
        if self.variable['_systemVars.systemFlags'] % self.variable['SF_CHOOSING'] * 2 > self.variable['SF_CHOOSING'] - 1:
            self.variable['_systemVars.systemFlags'] += 0 - self.variable['SF_CHOOSING']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        event_broadcastandwait
        event_broadcastandwait

    async def on_Logicframes_88(self):
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 2] == "0":
            procedures_call
        else:
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 19] = "0"
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
            event_broadcastandwait

    async def on_Logicpause_89(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 21] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 21] - 1
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 21] == "0":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
            event_broadcastandwait

    async def on_LogicwaitSync_90(self):
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 2] == "0":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
            event_broadcastandwait

    async def on_LogicsimpleAnim_91(self):
        procedures_call

    async def on_LogicrunGetOff_92(self):
        self.variable['getOff'] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.GET_OFF']]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.GET_OFF']] = "0"
        if not self.variable['getOff'] == "0":
            procedures_call

    async def on_LogiccheckModuleLoaded_93(self):
        self.lists['Params'].append("Logic.checkModuleLoaded")
        event_broadcastandwait

    async def on_LogicfnExec_94(self):
        self.lists['Params'].append("Logic.fnExec")
        event_broadcastandwait

    async def on_LogicinitScriptVariables_95(self):
        event_broadcastandwait
        self.variable['initialisationString'] = self.variable['Return value']
        self.variable['i'] = "0"
        for _ in range(838):
            procedures_call
            self.lists['Logic._ScriptVariables'][self.variable['i'] / 4 + 1] = self.variable['Return value']
            self.variable['i'] += 4
        self.variable['initialisationString'] = ""

    async def on_LogicmouseScript_96(self):
        self.variable['scriptComp'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['scrNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['tmpComp'] = self.variable['_compact']
        self.variable['_compact'] = self.variable['scriptComp']
        procedures_call
        self.variable['retVal'] = self.variable['Return value']
        self.variable['_compact'] = self.variable['tmpComp']
        if self.variable['scrNum'] == "14" or not self.variable['scrNum'] < "24578" and not self.variable['scrNum'] > "24584":
            procedures_call
        self.variable['Return value'] = self.variable['retVal']

    async def on_Logicscript_97(self):
        self.variable['offsetParam'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['scriptNoParam'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call

    async def on_LogicfnCacheChip_98(self):
        event_broadcastandwait
        self.lists['Params'].append(self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnCacheFast_99(self):
        self.lists['Params'].append(self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnDrawScreen_100(self):
        self.variable['_SystemVars.currentPalette'] = self.variable['a']
        self.lists['Params'].append(self.variable['a'])
        self.lists['Params'].append(self.variable['b'])
        event_broadcastandwait
        if self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCREEN']] == "32":
            event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnAr_101(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 19] = "1"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 51] = self.variable['a']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 52] = self.variable['b']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "2"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 6] = operator_mathop * 8
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 7] = operator_mathop * 8
        self.variable['Return value'] = "false"

    async def on_LogicfnArAnimate_102(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 22] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "3"
        self.variable['Return value'] = "false"

    async def on_LogicfnIdle_103(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnInteract_104(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 4
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "1"
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 17])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 2)
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.variable['Return value'] = "false"

    async def on_LogicfnStartSub_105(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 4
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26])
        self.lists['Params'].append(self.variable['a'] % 65536)
        event_broadcastandwait
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 2)
        self.lists['Params'].append(operator_mathop)
        event_broadcastandwait
        self.variable['Return value'] = "false"

    async def on_LogicfnTheyStartSub_106(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 26] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 26] + 4
        self.lists['Params'].append(self.variable['cpt'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 26])
        self.lists['Params'].append(self.variable['b'] % 65536)
        event_broadcastandwait
        self.lists['Params'].append(self.variable['cpt'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 26] + 2)
        self.lists['Params'].append(operator_mathop)
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnAssignBase_107(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 26] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['cpt']] = "1"
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 27] = self.variable['b'] % 65536
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 28] = operator_mathop
        self.variable['Return value'] = "true"

    async def on_LogicfnDiskMouse_108(self):
        self.lists['Params'].append("2")
        self.lists['Params'].append("11")
        self.lists['Params'].append("11")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnNormalMouse_109(self):
        self.lists['Params'].append("1")
        self.lists['Params'].append("0")
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnBlankMouse_110(self):
        procedures_call

    async def on_LogicfnCrossMouse_111(self):
        procedures_call

    async def on_LogicfnCursorRight_112(self):
        self.lists['Params'].append("4")
        self.lists['Params'].append("9")
        self.lists['Params'].append("4")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnCursorLeft_113(self):
        self.lists['Params'].append("5")
        self.lists['Params'].append("0")
        self.lists['Params'].append("5")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnCursorDown_114(self):
        self.lists['Params'].append("3")
        self.lists['Params'].append("9")
        self.lists['Params'].append("4")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnCursorUp_115(self):
        self.lists['Params'].append("8")
        self.lists['Params'].append("9")
        self.lists['Params'].append("4")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnOpenHand_116(self):
        self.lists['Params'].append("true")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnCloseHand_117(self):
        self.lists['Params'].append("false")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnGetTo_118(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 18] = self.variable['b']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 4
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 4]
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 5]
        self.variable['getToTable'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        while not self.lists['SkyCompact._RawBuff'][self.variable['getToTable']] == self.variable['a']:
            self.variable['getToTable'] += 2
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['getToTable'] + 1])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] + 2)
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.variable['Return value'] = "false"

    async def on_LogicfnSetToStand_119(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 22] = "1"
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(138 + self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 54] + self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 35] * 4)
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = self.lists['SkyCompact._RawBuff'][self.variable['Return value']]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = "0"
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.variable['standList'] = self.variable['Return value']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 25] = self.lists['SkyCompact._RawBuff'][self.variable['standList']]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "16"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] + 1
        procedures_call
        self.variable['Return value'] = "false"

    async def on_LogicfnTurnTo_120(self):
        self.variable['curDir'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 35]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 35] = self.variable['a'] % 65536
        self.lists['Params'].append(self.variable['_compact'])
        self.lists['Params'].append(self.variable['curDir'])
        event_broadcastandwait
        self.variable['tt'] = self.variable['Return value']
        if self.lists['SkyCompact._RawBuff'][self.variable['tt'] + self.variable['a']] == "0":
            self.variable['Return value'] = "true"
            control_stop
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 48] = self.lists['SkyCompact._RawBuff'][self.variable['tt'] + self.variable['a']]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 49] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "7"
        event_broadcastandwait
        self.variable['Return value'] = "false"

    async def on_LogicfnArrived_121(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 38] = self.variable['a'] % 65536
        self.lists['Logic._ScriptVariables'][self.variable['a'] / 4 + 1] = self.lists['Logic._ScriptVariables'][self.variable['a'] / 4 + 1] + 1
        self.variable['Return value'] = "true"

    async def on_LogicfnLeaving_122(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 39] = "0"
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 38] == "0":
            self.lists['Logic._ScriptVariables'][self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 38] / 4 + 1] = self.lists['Logic._ScriptVariables'][self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 38] / 4 + 1] - 1
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 38] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnSetAlternate_123(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 41] = self.variable['a'] % 65536
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "5"
        self.variable['Return value'] = "false"

    async def on_LogicfnAltSetAlternate_124(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 41] = self.variable['b'] % 65536
        self.lists['SkyCompact._RawBuff'][self.variable['cpt']] = "5"
        self.variable['Return value'] = "false"

    async def on_LogicfnKillId_125(self):
        if not self.variable['a'] == "0":
            self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
            if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] % 256 > "127":
                self.lists['Params'].append(self.variable['cpt'])
                event_broadcastandwait
            if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8] < "0":
                self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8])
                event_broadcastandwait
            self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnNoHuman_126(self):
        procedures_call

    async def on_LogicfnAddHuman_127(self):
        event_broadcastandwait

    async def on_LogicfnAddButtons_128(self):
        if self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STATUS']] % 8 < "4":
            self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STATUS']] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STATUS']] + 4
        self.variable['Return value'] = "true"

    async def on_LogicfnNoButtons_129(self):
        if self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STATUS']] % 8 > "3":
            self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STATUS']] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STATUS']] - 4
        self.variable['Return value'] = "true"

    async def on_LogicfnSetStop_130(self):
        if self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STOP']] % 2 < "1":
            self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STOP']] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STOP']] + 1
        self.variable['Return value'] = "true"

    async def on_LogicfnClearStop_131(self):
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MOUSE_STOP']] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnPointerText_132(self):
        self.lists['Params'].append(self.variable['a'])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnQuit_133(self):
        self.variable['Return value'] = "false"

    async def on_LogicfnSpeakMe_134(self):
        procedures_call

    async def on_LogicfnSpeakMeDir_135(self):
        self.variable['animNum'] = self.variable['c']
        self.variable['animNum'] += self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 35] * 2
        procedures_call

    async def on_LogicfnSpeakWait_136(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 21] = self.variable['a'] % 65536
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "10"
        event_broadcastandwait

    async def on_LogicfnSpeakWaitDir_137(self):
        procedures_call

    async def on_LogicfnChooser_138(self):
        self.lists['Params'].append(self.variable['_systemVars.systemFlags'])
        self.lists['Params'].append(self.variable['SF_CHOOSING'])
        event_broadcastandwait
        self.variable['_systemVars.systemFlags'] = self.variable['Return value']
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.THE_CHOSEN_ONE']] = "0"
        self.variable['p'] = self.variable['scriptVariableOffsets.TEXT1']
        self.variable['ycood'] = "136"
        while not self.lists['Logic._ScriptVariables'][self.variable['p']] == "0":
            self.variable['textNum'] = self.lists['Logic._ScriptVariables'][self.variable['p']]
            self.variable['p'] += 1
            self.lists['Params'].append(self.variable['textNum'])
            self.lists['Params'].append("320")
            self.lists['Params'].append("0")
            self.lists['Params'].append("241")
            self.lists['Params'].append("0")
            event_broadcastandwait
            self.lists['Params'].append(self.variable['Return value'])
            event_broadcastandwait
            self.variable['textCompact'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['Return value'] / 4096 + 1] + self.variable['Return value'] % 4096]
            self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 20] = self.variable['textNum']
            self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 19] = self.lists['Logic._ScriptVariables'][self.variable['p']]
            self.variable['p'] += 1
            self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 1])
            self.lists['Params'].append("16")
            event_broadcastandwait
            self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 1] = self.variable['Return value']
            self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 6] = "128"
            self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 7] = self.variable['ycood']
            self.variable['ycood'] += 12
            self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 6] - 128)
            self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 7] - 130)
            self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 8])
            event_broadcastandwait
        if self.variable['p'] == self.variable['scriptVariableOffsets.TEXT1']:
            self.variable['Return value'] = "true"
            control_stop
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "12"
        event_broadcastandwait
        self.lists['Params'].append(self.variable['p'] - self.variable['scriptVariableOffsets.TEXT1'] / 2)
        event_broadcastandwait
        event_broadcastandwait
        self.variable['Return value'] = "false"

    async def on_LogicfnHighlight_139(self):
        self.variable['pen'] = self.variable['b']
        self.variable['pen'] += -11
        if self.variable['pen'] % 2 == "0":
            self.variable['pen'] += 1
        else:
            self.variable['pen'] += -1
        self.variable['pen'] += 241
        self.variable['textCompact'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Params'].append(self.variable['textCompact'] + 21)
        event_broadcastandwait
        self.variable['sprData'] = self.variable['Return value']
        self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 8])
        self.lists['Params'].append(self.variable['pen'] % 256)
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnTextKill_140(self):
        self.variable['id'] = "23"
        for _ in range(10):
            self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['id'] / 4096 + 1] + self.variable['id'] % 4096]
            if self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] % 32 > "15":
                self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "0"
                self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8])
                event_broadcastandwait
            self.variable['id'] += 1
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnStopMode_141(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "11"
        self.variable['Return value'] = "false"

    async def on_LogicfnWeWait_142(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 50] = self.variable['a']
        procedures_call

    async def on_LogicfnSendSync_143(self):
        self.lists['SkyCompact._RawBuff'][self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096] + 2] = self.variable['b'] % 65536
        self.variable['Return value'] = "false"

    async def on_LogicfnSendFastSync_144(self):
        self.lists['SkyCompact._RawBuff'][self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096] + 2] = self.variable['b'] % 65536
        self.variable['Return value'] = "true"

    async def on_LogicfnSendRequest_145(self):
        self.lists['SkyCompact._RawBuff'][self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096] + 42] = self.variable['b'] % 65536
        self.variable['Return value'] = "false"

    async def on_LogicfnClearRequest_146(self):
        self.lists['SkyCompact._RawBuff'][self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096] + 42] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnCheckRequest_147(self):
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 42] == "0":
            self.variable['Return value'] = "true"
            control_stop
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 26] = "4"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 29] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 42]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 30] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 42] = "0"
        self.variable['Return value'] = "false"

    async def on_LogicfnStartMenu_148(self):
        self.variable['firstObject'] = self.variable['a'] / 4 + 1
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][1] + 47]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "90"
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCREEN']] % 65536
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][1] + 48]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "90"
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCREEN']] % 65536
        self.variable['menuLength'] = "0"
        self.variable['i'] = self.variable['firstObject']
        for _ in range(30):
            if not self.lists['Logic._ScriptVariables'][self.variable['i']] == "0":
                self.variable['menuLength'] += 1
                self.lists['_objectList'][self.variable['menuLength']] = self.lists['Logic._ScriptVariables'][self.variable['i']]
            self.variable['i'] += 1
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MENU_LENGTH']] = self.variable['menuLength']
        self.variable['blankID'] = "51"
        self.variable['i'] = self.variable['menuLength']
        while not self.variable['i'] > "10":
            self.lists['_objectList'][self.variable['i'] + 1] = self.variable['blankID']
            self.variable['blankID'] += 1
            self.variable['i'] += 1
        self.variable['break?'] = "false"
        self.variable['i'] = "0"
        while not self.variable['i'] == "30" or self.variable['break?'] == "true":
            if not self.lists['_objectList'][self.variable['i'] + 1] == "0":
                self.variable['temp'] = self.lists['_objectList'][self.variable['i'] + 1]
                self.lists['SkyCompact._RawBuff'][self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096] + 1] = "64"
                self.variable['i'] += 1
            else:
                self.variable['break?'] = "true"
        if self.variable['menuLength'] < "11":
            self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCROLL_OFFSET']] = "0"
        else:
            if self.variable['menuLength'] < self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCROLL_OFFSET']] + 11:
                self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCROLL_OFFSET']] = self.variable['menuLength'] - 11
        self.variable['rollingX'] = "156"
        self.variable['i'] = "0"
        for _ in range(11):
            self.variable['temp'] = self.lists['_objectList'][self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCROLL_OFFSET']] + self.variable['i'] + 1]
            self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
            self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "90"
            self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3] = self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.SCREEN']] % 65536
            self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 6] = self.variable['rollingX']
            self.variable['rollingX'] += 24
            if self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.MENU']] == "2":
                self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 7] = "136"
            else:
                self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 7] = "112"
            self.variable['i'] += 1
        self.variable['Return value'] = "true"

    async def on_LogicfnFaceId_149(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.variable['x'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 6] - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 6]
        procedures_call
        self.variable['x'] = self.variable['Return value']
        if self.variable['x'] < "0":
            self.variable['x'] = 0 - self.variable['x']
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 20] = "3"
        else:
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 20] = "2"
        self.variable['y'] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 7] - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 7] + self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 14] + self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 16]
        procedures_call
        self.variable['y'] = self.variable['Return value']
        if self.variable['y'] < "0":
            self.variable['y'] = 0 - self.variable['y']
            if not self.variable['y'] < self.variable['x']:
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 20] = "1"
        else:
            if not self.variable['y'] < self.variable['x']:
                self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 20] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnForeground_150(self):
        self.variable['temp'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = operator_mathop * 8
        if self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] % 4 < "2":
            self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] + 2
        self.variable['Return value'] = "true"

    async def on_LogicfnBackground_151(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] = operator_mathop * 8
        if self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] % 2 < "1":
            self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] + 1
        self.variable['Return value'] = "true"

    async def on_LogicfnNewBackground_152(self):
        self.variable['temp'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = operator_mathop * 8
        if self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] % 2 < "1":
            self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] + 1
        self.variable['Return value'] = "true"

    async def on_LogicfnSort_153(self):
        self.variable['temp'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = operator_mathop * 8
        if self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] % 8 < "4":
            self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] + 4
        self.variable['Return value'] = "true"

    async def on_LogicfnNoSpriteEngine_154(self):
        self.lists['_logicTable'][self.variable['_compact'] + 1] = operator_mathop * 8
        self.variable['Return value'] = "true"

    async def on_LogicfnNoSpritesA_155(self):
        self.variable['temp'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['temp'] + 1] = operator_mathop * 8
        self.variable['Return value'] = "true"

    async def on_LogicfnResetId_156(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.variable['rst'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['b'] / 4096 + 1] + self.variable['b'] % 4096]
        while True:
            self.variable['off'] = self.lists['SkyCompact._RawBuff'][self.variable['rst']]
            self.variable['rst'] += 1
            if self.variable['off'] == "65535":
                self.variable['Return value'] = "true"
                control_stop
            self.lists['Params'].append(self.variable['cpt'])
            self.lists['Params'].append(self.variable['off'])
            event_broadcastandwait
            self.lists['SkyCompact._RawBuff'][self.variable['Return value']] = self.lists['SkyCompact._RawBuff'][self.variable['rst']]
            self.variable['rst'] += 1

    async def on_LogicfnToggleGrid_157(self):
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1])
        self.lists['Params'].append("128")
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 1] = self.variable['Return value']
        self.variable['Return value'] = "true"

    async def on_LogicfnPause_158(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 21] = self.variable['a'] % 65536
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "14"
        self.variable['Return value'] = "false"

    async def on_LogicfnRunAnimMod_159(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = self.variable['a']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = "0"
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 25] = self.lists['SkyCompact._RawBuff'][self.variable['Return value']]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] + 1
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "6"
        procedures_call
        self.variable['Return value'] = "false"

    async def on_LogicfnSimpleMod_160(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = self.variable['a']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "16"
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 25] = self.lists['SkyCompact._RawBuff'][self.variable['Return value']]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] + 1
        procedures_call
        self.variable['Return value'] = "false"

    async def on_LogicfnRunFrames_161(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 23] = self.variable['a']
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = "0"
        self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "13"
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 25] = self.lists['SkyCompact._RawBuff'][self.variable['Return value']]
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 24] + 1
        procedures_call
        self.variable['Return value'] = "false"

    async def on_LogicfnAwaitSync_162(self):
        if not self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 2] == "0":
            self.variable['Return value'] = "true"
        else:
            self.lists['SkyCompact._RawBuff'][self.variable['_compact']] = "15"
            self.variable['Return value'] = "false"

    async def on_LogicfnIncMegaSet_163(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 54] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 54] + 144
        self.variable['Return value'] = "true"

    async def on_LogicfnDecMegaSet_164(self):
        self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 54] = self.lists['SkyCompact._RawBuff'][self.variable['_compact'] + 54] - 144
        self.variable['Return value'] = "true"

    async def on_LogicfnSetMegaSet_165(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 54] = self.variable['b'] * 144
        self.variable['Return value'] = "true"

    async def on_LogicfnMoveItems_166(self):
        self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][1] + 189] + self.variable['a']]
        self.variable['p'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
        for _ in range(2):
            if self.lists['SkyCompact._RawBuff'][self.variable['p']] == "0":
                self.variable['Return value'] = "true"
                control_stop
            self.variable['temp'] = self.lists['SkyCompact._RawBuff'][self.variable['p']]
            self.variable['p'] += 1
            self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['temp'] / 4096 + 1] + self.variable['temp'] % 4096]
            self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3] = self.variable['b'] % 65536
            self.variable['Return value'] = "true"
        self.variable['Return value'] = "true"

    async def on_LogicfnNewList_167(self):
        self.variable['i'] = "0"
        for _ in range(16):
            self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.TEXT1'] + self.variable['i']] = "0"
            self.variable['i'] += 1
        self.variable['Return value'] = "true"

    async def on_LogicfnAskThis_168(self):
        self.variable['p'] = self.variable['scriptVariableOffsets.TEXT1']
        while not self.lists['Logic._ScriptVariables'][self.variable['p']] == "0":
            self.variable['p'] += 2
        self.lists['Logic._ScriptVariables'][self.variable['p']] = self.variable['a']
        self.variable['p'] += 1
        self.lists['Logic._ScriptVariables'][self.variable['p']] = self.variable['b']
        self.variable['Return value'] = "true"

    async def on_LogicfnRandom_169(self):
        self.lists['Params'].append(random.randint(0, 65535))
        self.lists['Params'].append(self.variable['a'])
        event_broadcastandwait
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RND']] = self.variable['Return value']
        self.variable['Return value'] = "true"

    async def on_LogicfnPersonHere_170(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RESULT']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3] == self.variable['b'] * 1
        self.variable['Return value'] = "true"

    async def on_LogicfnToggleMouse_171(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1])
        self.lists['Params'].append("16")
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = self.variable['Return value']
        self.variable['Return value'] = "true"

    async def on_LogicfnMouseOn_172(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1])
        self.lists['Params'].append("16")
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = self.variable['Return value']
        self.variable['Return value'] = "true"

    async def on_LogicfnMouseOff_173(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1])
        self.lists['Params'].append(65535 - 16)
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = self.variable['Return value']
        self.variable['Return value'] = "true"

    async def on_LogicfnFetchX_174(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RESULT']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 6]
        self.variable['Return value'] = "true"

    async def on_LogicfnFetchY_175(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RESULT']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 7]
        self.variable['Return value'] = "true"

    async def on_LogicfnTestList_176(self):
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RESULT']] = "0"
        self.variable['list'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        while not self.lists['SkyCompact._RawBuff'][self.variable['list']] == "0":
            if not self.variable['b'] < self.lists['SkyCompact._RawBuff'][self.variable['list']] and self.variable['b'] < self.lists['SkyCompact._RawBuff'][self.variable['list'] + 1] and not self.variable['c'] < self.lists['SkyCompact._RawBuff'][self.variable['list'] + 2] and self.variable['c'] < self.lists['SkyCompact._RawBuff'][self.variable['list'] + 3]:
                self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RESULT']] = self.lists['SkyCompact._RawBuff'][self.variable['list'] + 4]
            self.variable['list'] += 5
        self.variable['Return value'] = "true"

    async def on_LogicfnFetchPlace_177(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.RESULT']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 4]
        self.variable['Return value'] = "true"

    async def on_LogicfnCustomJoey_178(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.PLAYER_X']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 6]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.PLAYER_Y']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 7]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.PLAYER_MOOD']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 22]
        self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.PLAYER_SCREEN']] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 3]
        self.variable['Return value'] = "true"

    async def on_LogicfnSetPalette_179(self):
        self.lists['Params'].append("Logic.fnSetPalette")
        event_broadcastandwait

    async def on_LogicfnTextModule_180(self):
        self.lists['Params'].append(self.variable['a'])
        self.lists['Params'].append(self.variable['b'])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnChangeName_181(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['Logic._ScriptVariables'][self.variable['cpt'] + 9] = self.variable['b']
        self.variable['Return value'] = "true"

    async def on_LogicfnMiniLoad_182(self):
        self.lists['Params'].append(self.variable['a'])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnFlushBuffers_183(self):
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnFlushChip_184(self):
        self.variable['Return value'] = "true"

    async def on_LogicfnSaveCoods_185(self):
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnPlotGrid_186(self):
        self.lists['Params'].append(self.variable['a'])
        self.lists['Params'].append(self.variable['b'])
        self.lists['Params'].append(self.variable['c'])
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait

    async def on_LogicfnRemoveGrid_187(self):
        self.lists['Params'].append(self.variable['a'])
        self.lists['Params'].append(self.variable['b'])
        self.lists['Params'].append(self.variable['c'])
        self.lists['Params'].append(self.variable['_compact'])
        event_broadcastandwait

    async def on_LogicfnEyeball_188(self):
        self.lists['Params'].append("Logic.fnEyeball")
        event_broadcastandwait

    async def on_LogicfnRestoreGame_189(self):
        self.lists['Params'].append("Logic.fnRestoreGame")
        event_broadcastandwait

    async def on_LogicfnRestartGame_190(self):
        event_broadcastandwait
        self.variable['Return value'] = "false"

    async def on_LogicfnNewSwingSeq_191(self):
        if self.variable['a'] == "85" or self.variable['a'] == "106" or self.variable['a'] == "75" or self.variable['a'] == "15":
            self.lists['Params'].append(self.variable['a'])
            event_broadcastandwait
        else:
            SUBSTACK2
        self.variable['Return value'] = "true"

    async def on_LogicfnWaitSwingEnd_192(self):
        self.lists['Params'].append("Logic.fnWaitSwingEnd")
        event_broadcastandwait

    async def on_LogicfnSkipIntroCode_193(self):
        self.variable['_SystemVars.pastIntro'] = "true"
        self.variable['Return value'] = "true"

    async def on_LogicfnBlankScreen_194(self):
        self.lists['Params'].append("Logic.fnBlankScreen")
        event_broadcastandwait

    async def on_LogicfnPrintCredit_195(self):
        self.lists['Params'].append("Logic.fnPrintCredit")
        event_broadcastandwait

    async def on_LogicfnLookAt_196(self):
        self.lists['Params'].append(self.variable['a'])
        self.lists['Params'].append("240")
        self.lists['Params'].append("0")
        self.lists['Params'].append("248")
        self.lists['Params'].append("true")
        event_broadcastandwait
        self.variable['textInfo'] = self.variable['Return value']
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait
        self.variable['textCpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['Return value'] / 4096 + 1] + self.variable['Return value'] % 4096]
        self.lists['Params'].append(168 - 148)
        self.lists['Params'].append(self.variable['c'] - 130)
        self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['textCpt'] + 8])
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        self.lists['Params'].append("true")
        event_broadcastandwait
        procedures_call
        event_broadcastandwait
        self.lists['Params'].append("800")
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        self.lists['SkyCompact._RawBuff'][self.variable['textCpt'] + 1] = "0"
        self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['textCpt'] + 8])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnLincTextModule_197(self):
        if self.variable['c'] > "32767":
            self.variable['cnt'] = self.variable['scriptVariableOffsets.LINC_DIGIT_0']
            for _ in range(10):
                self.lists['Logic._ScriptVariables'][self.variable['cnt']] = "0"
                self.variable['cnt'] += 1
        self.variable['buttonAction'] = self.variable['c'] % 32768
        if self.variable['buttonAction'] < "10":
            self.lists['Logic._ScriptVariables'][self.variable['scriptVariableOffsets.LINC_DIGIT_0'] + self.variable['buttonAction']] = self.variable['b']
        self.lists['Params'].append(self.variable['b'])
        self.lists['Params'].append("220")
        self.lists['Params'].append("0")
        self.lists['Params'].append("215")
        self.lists['Params'].append("false")
        event_broadcastandwait
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait
        self.variable['textCompact'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['Return value'] / 4096 + 1] + self.variable['Return value'] % 4096]
        if self.variable['a'] < "20":
            self.variable['xPos'] = "152"
            self.variable['yPos'] = self.variable['a'] * 13 + 170
        else:
            if self.variable['a'] > "20":
                self.variable['xPos'] = self.variable['a']
                self.variable['yPos'] = "214"
        self.lists['Params'].append(self.variable['xPos'] - 128)
        self.lists['Params'].append(self.variable['yPos'] - 130)
        self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 8])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnTextKill_198(self):
        self.variable['id'] = "23"
        for _ in range(10):
            self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['id'] / 4096 + 1] + self.variable['id'] % 4096]
            self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 1] = "0"
            self.lists['Params'].append(0 - self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8])
            event_broadcastandwait
            self.variable['id'] += 1
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnSetFont_199(self):
        self.lists['Params'].append(self.variable['a'])
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnStartFx_200(self):
        procedures_call

    async def on_LogicfnStopFx_201(self):
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnStartMusic_202(self):
        if self.variable['_systemVars.systemFlags'] % self.variable['SF_MUS_OFF'] * 2 < self.variable['SF_MUS_OFF']:
            self.lists['Params'].append(self.variable['a'])
            event_broadcastandwait
        self.variable['_SystemVars.currentMusic'] = self.variable['a']
        self.variable['Return value'] = "true"

    async def on_LogicfnStopMusic_203(self):
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.variable['_SystemVars.currentMusic'] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicfnFadeDown_204(self):
        self.lists['Params'].append("Logic.fnFadeDown")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnFadeUp_205(self):
        self.lists['Params'].append("Logic.fnFadeUp")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnQuitToDos_206(self):
        self.lists['Params'].append("Logic.fnQuitToDos")
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnPauseFx_207(self):
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnUnPauseFx_208(self):
        event_broadcastandwait
        self.variable['Return value'] = "true"

    async def on_LogicfnPrintf_209(self):
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("fnPrintf(" + self.variable['a'] + ", " + self.variable['b'] + ", " + self.variable['c'] + ")")
            event_broadcastandwait

    async def on_LogicuseControlInstance_210(self):
        procedures_call

    async def on_Scratchinitialise_211(self):
        procedures_call

    async def on_Scratchreset_212(self):
        self.variable['data'] = ""
        self.variable['scriptData'] = "0"
        self.lists['_objectList'] = []
        self.lists['Logic._ScriptVariables'] = []
        self.lists['_logicTable'] = []
        self.lists['_moduleList'] = []
        self.lists['_mcodeTable'] = []
        self.lists['_stack'] = []
        self.lists['script locals stack'] = []
        self.lists['allScriptData'] = []
        if sensing_of == "true":
            data_showvariable
            data_showvariable
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidevariable
        data_hidevariable
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist

    async def on_Logicanim_213(self):
        procedures_call

    async def on_LogicfnUnhighlight_214(self):
        self.variable['cpt'] = self.lists['SkyCompact._Compacts'][self.lists['SkyCompact._DataOffsets'][self.variable['a'] / 4096 + 1] + self.variable['a'] % 4096]
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8] = self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 8] - 1
        self.lists['SkyCompact._RawBuff'][self.variable['cpt'] + 20] = "0"
        self.variable['Return value'] = "true"

    async def on_LogicparseSaveData_215(self):
        self.variable['dataIndex'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        self.variable['cnt'] = "1"
        for _ in range(838):
            self.lists['Logic._ScriptVariables'][self.variable['cnt']] = self.lists['SaveGameData'][self.variable['dataIndex']] + self.lists['SaveGameData'][self.variable['dataIndex'] + 1] * 65536
            self.variable['cnt'] += 1
            self.variable['dataIndex'] += 2
        procedures_call


class skymouse(SpriteBase):
    async def on_newMouse_216(self):
        self.variable['_mouseB'] = "0"
        self.variable['_currentCursor'] = "6"
        self.variable['_mouseX'] = "160"
        self.variable['_mouseY'] = "96"
        self.lists['Params'].append("60300")
        event_broadcastandwait
        self.variable['_miceData'] = self.variable['Return value']
        self.lists['Params'].append("60301")
        event_broadcastandwait
        self.variable['_objectMouseData'] = self.variable['Return value']
        self.variable['_heldObject'] = "0"
        self.variable['mouseUp?'] = "false"

    async def on_MousereplaceMouseCursors_217(self):
        self.variable['fileNo'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append(self.variable['fileNo'])
        event_broadcastandwait
        self.variable['_objectMouseData'] = self.variable['Return value']

    async def on_MousefnAddHuman_218(self):
        if self.lists['Logic._ScriptVariables'][sensing_of] == "0":
            self.lists['Params'].append(self.lists['Logic._ScriptVariables'][sensing_of])
            self.lists['Params'].append("6")
            event_broadcastandwait
            self.lists['Logic._ScriptVariables'][sensing_of] = self.variable['Return value']
            if self.variable['_mouseY'] < "2":
                self.variable['_mouseY'] = "2"
            if not self.lists['Logic._ScriptVariables'][sensing_of] == "0":
                self.lists['Params'].append(self.lists['Logic._ScriptVariables'][sensing_of] % 65536)
                self.lists['Params'].append(operator_mathop)
                event_broadcastandwait
            self.lists['Logic._ScriptVariables'][sensing_of] = "4294967295"
            self.lists['Logic._ScriptVariables'][sensing_of] = "23"
        self.variable['Return value'] = "true"

    async def on_MousefnSaveCoods_219(self):
        self.lists['Logic._ScriptVariables'][sensing_of] = self.variable['_mouseX'] + 128
        self.lists['Logic._ScriptVariables'][sensing_of] = self.variable['_mouseY'] + self.variable['TOP_LEFT_Y']

    async def on_MouselockMouse_220(self):
        if self.variable['_systemVars.systemFlags'] % self.variable['SF_MOUSE_LOCKED'] * 2 < self.variable['SF_MOUSE_LOCKED']:
            self.variable['_systemVars.systemFlags'] += self.variable['SF_MOUSE_LOCKED']

    async def on_MouseunlockMouse_221(self):
        if not self.variable['_systemVars.systemFlags'] % self.variable['SF_MOUSE_LOCKED'] * 2 < self.variable['SF_MOUSE_LOCKED']:
            self.variable['_systemVars.systemFlags'] += 0 - self.variable['SF_MOUSE_LOCKED']

    async def on_MouserestoreMouseData_222(self):
        pass

    async def on_MousedrawNewMouse_223(self):
        pass

    async def on_MousewaitMouseNotPressed_224(self):
        self.variable['minDelay'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['mousePressed'] = "true"
        event_broadcastandwait
        self.variable['now'] = self.variable['Return value']
        while not not self.variable['mousePressed'] == "true" or self.variable['Return value'] < self.variable['now'] + self.variable['minDelay']:
            self.variable['mousePressed'] = sensing_mousedown
            if sensing_keypressed:
                self.variable['minDelay'] = "0"
                self.variable['mousePressed'] = "false"
            event_broadcastandwait

    async def on_MousespriteMouse_225(self):
        self.variable['mouseY'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['mouseX'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['frameNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['_currentCursor'] = self.variable['frameNum']
        procedures_call
        self.variable['mouseWidth'] = self.variable['Return value']
        procedures_call
        self.variable['mouseHeight'] = self.variable['Return value']
        self.variable['hotspotX'] = self.variable['mouseX']
        self.variable['hotspotY'] = self.variable['mouseY']
        if self.variable['frameNum'] > "0":
            self.variable['_heldObject'] = "0"

    async def on_MousemouseEngine_226(self):
        self.variable['_logicClick'] = self.variable['_mouseB'] > "0"
        if self.lists['Logic._ScriptVariables'][sensing_of] == "0":
            if self.lists['Logic._ScriptVariables'][sensing_of] % 4 > "1":
                procedures_call
                if self.lists['Logic._ScriptVariables'][sensing_of] % 8 > "2":
                    procedures_call
        self.variable['_mouseB'] = "0"

    async def on_MousebuttonPressed_227(self):
        self.lists['Params'].append("Mouse.buttonPressed should not be called")
        event_broadcastandwait

    async def on_MousemouseMoved_228(self):
        self.lists['Params'].append("Mouse.mouseMoved should not be called")
        event_broadcastandwait

    async def on_MouseresetCursor_229(self):
        self.lists['Params'].append(self.variable['_currentCursor'])
        self.lists['Params'].append("0")
        self.lists['Params'].append("0")
        event_broadcastandwait

    async def on_MousefindMouseCursor_230(self):
        self.variable['itemNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['cnt'] = "0"
        for _ in range(24):
            if self.variable['itemNum'] == self.lists['_mouseMainObjects'][self.variable['cnt'] + 1]:
                self.variable['Return value'] = self.variable['cnt']
                control_stop
            self.variable['cnt'] += 1
        self.variable['cnt'] = "0"
        for _ in range(21):
            if self.variable['itemNum'] == self.lists['_mouseLincObjects'][self.variable['cnt'] + 1]:
                self.variable['Return value'] = self.variable['cnt']
                control_stop
            self.variable['cnt'] += 1
        self.variable['Return value'] = "0"

    async def on_MousefnOpenCloseHand_231(self):
        self.variable['open'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if self.variable['open'] == "false" and self.lists['Logic._ScriptVariables'][sensing_of] == "0":
            self.variable['_heldObject'] = "0"
            self.lists['Params'].append("1")
            self.lists['Params'].append("0")
            self.lists['Params'].append("0")
            event_broadcastandwait
            control_stop
        self.lists['Params'].append(self.lists['Logic._ScriptVariables'][sensing_of])
        event_broadcastandwait
        self.variable['cursor'] = self.variable['Return value'] * 2
        if self.variable['open'] == "true":
            self.variable['cursor'] += 1
        self.variable['_heldObject'] = self.variable['cursor']
        self.lists['Params'].append("0")
        self.lists['Params'].append("5")
        self.lists['Params'].append("5")
        event_broadcastandwait

    async def on_MousewasClicked_232(self):
        if self.variable['_logicClick'] == "true":
            self.variable['_logicClick'] = "false"
            self.variable['Return value'] = "true"
        else:
            self.variable['Return value'] = "false"

    async def on_MouseuseLogicInstance_233(self):
        pass

    async def on_MousegiveMouseX_234(self):
        self.variable['Return value'] = self.variable['_mouseX']

    async def on_MousegiveMouseY_235(self):
        self.variable['Return value'] = self.variable['_mouseY']

    async def on_MousegiveCurrentMouseType_236(self):
        self.variable['Return value'] = self.variable['_currentCursor']

    async def on_MouselogicClick_237(self):
        self.variable['_logicClick'] = "true"

    async def on_Scratchreset_238(self):
        self.variable['_miceData'] = ""
        self.variable['_objectMouseData'] = ""
        self.variable['frameNum'] = "0"
        self.visible = 0

    async def on_blitmouse_239(self):
        self.size = self.variable['Scale'] * 100
        if self.variable['_heldObject'] > "0":
            self.switch_costume("60301" + "_" + self.variable['_heldObject'])
            self.xpos = self.variable['_mouseX'] - 160 + self.variable['mouseWidth'] / 2 - 5 * self.variable['Scale']
            self.ypos = 36 + 100 - self.variable['_mouseY'] - self.variable['mouseHeight'] / 2 + 5 * self.variable['Scale']
        else:
            self.switch_costume("60300" + "_" + self.variable['frameNum'])
            self.xpos = self.variable['_mouseX'] - 160 + self.variable['mouseWidth'] / 2 - self.variable['hotspotX'] * self.variable['Scale']
            self.ypos = 36 + 100 - self.variable['_mouseY'] - self.variable['mouseHeight'] / 2 + self.variable['hotspotY'] * self.variable['Scale']
        if self.variable['frameNum'] == "6" or "-108" > sensing_mousey:
            self.visible = 0
        else:
            self.visible = 1

    async def on_mouseupdateMouse_240(self):
        self.variable['_mouseX'] = sensing_mousex / self.variable['Scale'] + 160
        self.variable['_mouseY'] = 100 - sensing_mousey + -36 / self.variable['Scale']
        if self.variable['_mouseX'] < "0":
            self.variable['_mouseX'] = "0"
        else:
            if self.variable['_mouseX'] > "320":
                self.variable['_mouseX'] = "320"
        if self.variable['_mouseY'] < "4":
            self.variable['_mouseY'] = "4"
        else:
            if self.variable['_mouseY'] > "192":
                self.variable['_mouseY'] = "192"
        if sensing_mousedown:
            if self.variable['mouseUp?'] == "true":
                self.variable['_mouseB'] = 1 + self.variable['Toolbar.useActive?'] == "false"
                self.variable['mouseUp?'] = "false"
        else:
            self.variable['mouseUp?'] = "true"


class skymusicbase(SpriteBase):
    async def on_newMusicBase_241(self):
        if self.variable['clone?'] == "false":
            self.variable['_currentMusic'] = "0"
            self.variable['_musicVolume'] = "50"
            self.variable['_currentMusic'] = "0"
            self.variable['MusicBase.IsPlaying?'] = "false"

    async def on_deleteMusicBase_242(self):
        if self.variable['clone?'] == "false":
            self.lists['Params'].append("delete MusicBase")
            event_broadcastandwait

    async def on_MusicBaseloadSection_243(self):
        if self.variable['clone?'] == "false":
            self.variable['pSection'] = self.lists['Params'][len(self.lists['Params'])]
            self.lists['Params'].pop(len(self.lists['Params']))
            self.variable['_currentSection'] = self.variable['pSection']
            self.variable['_onNextPoll.musicToProcess'] = "0"

    async def on_MusicBasemusicIsPlaying_244(self):
        if self.variable['clone?'] == "false":
            self.variable['Return value'] = self.variable['MusicBase.IsPlaying?']

    async def on_MusicBasestartMusic_245(self):
        if self.variable['clone?'] == "false":
            self.variable['param'] = self.lists['Params'][len(self.lists['Params'])]
            self.lists['Params'].pop(len(self.lists['Params']))
            self.variable['_onNextPoll.musicToProcess'] = self.variable['param'] % 16
            procedures_call

    async def on_MusicBasestopMusic_246(self):
        if self.variable['clone?'] == "true":
            control_delete_this_clone
        else:
            self.variable['MusicBase.IsPlaying?'] = "false"

    async def on_MusicBasegiveVolume_247(self):
        if self.variable['clone?'] == "false":
            self.lists['Params'].append("MusicBase.giveVolume")
            event_broadcastandwait

    async def on_MusicBasegiveCurrentMusic_248(self):
        if self.variable['clone?'] == "false":
            self.variable['Return value'] = self.variable['_currentMusic']

    async def on_MusicBasesetVolume_249(self):
        if self.variable['clone?'] == "false":
            self.lists['Params'].append("MusicBase.setVolume")
            event_broadcastandwait

    async def on_MusicBaseupdateTempo_250(self):
        if self.variable['clone?'] == "false":
            self.lists['Params'].append("MusicBase.updateTempo")
            event_broadcastandwait

    async def clone_start1(self):
        self.variable['clone?'] = "true"
        self.variable['MusicBase.IsPlaying?'] = "true"
        sound_setvolumeto
        while True:
            sound_playuntildone
            if self.variable['loops'] == "false":
                self.variable['MusicBase.IsPlaying?'] = "false"
                control_stop

    async def on_Scratchinitialise_251(self):
        self.variable['clone?'] = "false"

    async def on_MusicsetEnabled_252(self):
        if self.variable['clone?'] == "true":
            sound_setvolumeto


class skyscreen(SpriteBase):
    async def on_newScreen_253(self):
        self.variable['_seqInfo.nextFrame'] = "0"
        self.variable['_seqInfo.framesLeft'] = "0"
        self.variable['_seqInfo.running'] = "false"

    async def on_ScreenclearScreen_254(self):
        self.variable['fullscreen'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        pen_clear

    async def on_ScreensetFocusRectangle_255(self):
        self.lists['Params'].append("Screen.setFocusRectangle")
        event_broadcastandwait

    async def on_ScreensetPaletteuint_256(self):
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("Screen.setPalette (uint8*): Serves no purpose")
            event_broadcastandwait

    async def on_ScreensetPaletteEndian_257(self):
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("Screen.setPaletteEndian: Serves no purpose")
            event_broadcastandwait

    async def on_ScreenhalvePalette_258(self):
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("Screen.halvePalette: Serves no purpose")
            event_broadcastandwait

    async def on_ScreensetPaletteuint_259(self):
        self.lists['Params'].pop(len(self.lists['Params']))
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("Screen.setPalette (uint16): Serves no purpose")
            event_broadcastandwait

    async def on_ScreenshowScreenuintybool_260(self):
        self.variable['fullscreen'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['filenum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['_blit.backdrop'] = self.variable['filenum']
        event_broadcastandwait

    async def on_ScreenshowScreenuintbool_261(self):
        self.lists['Params'].append("Screen.showScreen (uint8*, bool)")
        event_broadcastandwait

    async def on_Screenrecreate_262(self):
        if self.lists['Logic._ScriptVariables'][sensing_of] == "0":
            control_stop
        self.variable['_blit.backdrop'] = "-1"
        self.variable['temp'] = self.lists['Logic._ScriptVariables'][sensing_of]
        self.variable['i'] = "1"
        while not self.lists['SkyCompact._LoadedFilesList'][self.variable['i']] == "0":
            if self.lists['SkyCompact._LoadedFilesList'][self.variable['i']] % 2048 == self.variable['temp']:
                self.variable['_blit.backdrop'] = self.lists['SkyCompact._LoadedFilesList'][self.variable['i']]
                control_stop
            self.variable['i'] += 1

    async def on_Screenflip_263(self):
        self.variable['doUpdate'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if self.variable['doUpdate'] == "true":
            event_broadcast
            event_broadcast
            event_broadcast
            event_broadcast
            event_broadcast
            if self.variable['Debug.Grid?'] == "true":
                event_broadcast

    async def on_ScreenfnDrawScreen_264(self):
        self.variable['scroll'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['palette'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append(self.variable['scroll'])
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        self.lists['Params'].append("false")
        event_broadcastandwait
        self.lists['Params'].append(self.variable['palette'])
        self.lists['Params'].append(self.variable['scroll'])
        event_broadcastandwait

    async def on_ScreenfnFadeDown_265(self):
        self.variable['scroll'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if not self.variable['scroll'] == "123" and not self.variable['scroll'] == "321" or not self.variable['_systemVars.systemFlags'] % self.variable['SF_NO_SCROLL'] * 2 < self.variable['SF_NO_SCROLL']:
            event_broadcastandwait
        else:
            self.lists['Params'].append("Screen.fnFadeDown: scroll preparation")
            event_broadcastandwait

    async def on_ScreenpaletteFadeUpuint_266(self):
        event_broadcastandwait

    async def on_ScreenpaletteFadeUpuint_267(self):
        self.variable['fileNr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        event_broadcastandwait

    async def on_ScreenfnFadeUp_268(self):
        self.variable['scroll'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['palNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if not self.variable['scroll'] == "123" and not self.variable['scroll'] == "321":
            self.variable['scroll'] = "0"
        if self.variable['scroll'] == "0":
            self.lists['Params'].append("true")
            event_broadcastandwait
            event_broadcastandwait
        else:
            self.lists['Params'].append("Screen.fnFadeUp (scrolling left or right)")
            event_broadcastandwait

    async def on_ScreenwaitForSequence_269(self):
        self.lists['Params'].append("Screen.waitForSequence")
        event_broadcastandwait

    async def on_ScreenstartSequence_270(self):
        self.variable['_seqInfo.currentSequence'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        event_broadcastandwait
        self.variable['_seqInfo.nextFrame'] = self.variable['Return value'] + 60
        self.variable['_seqInfo.currentFrame'] = "0"
        procedures_call
        self.variable['_seqInfo.framesLeft'] = self.variable['Return value']
        self.variable['_seqInfo.running'] = "true"
        self.variable['_seqInfo.runningItem'] = "false"

    async def on_ScreenstartSequenceItem_271(self):
        self.variable['filenum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append("Screen.startSequenceItem")
        event_broadcastandwait
        event_broadcastandwait
        self.variable['_seqInfo.nextFrame'] = self.variable['Return value'] + 60
        self.variable['_seqInfo.currentFrame'] = "0"
        procedures_call
        self.variable['_seqInfo.framesLeft'] = self.variable['Return value']
        self.variable['_seqInfo.running'] = "true"
        self.variable['_seqInfo.runningItem'] = "true"

    async def on_ScreenstopSequence_272(self):
        self.variable['_seqInfo.running'] = "false"
        self.variable['_seqInfo.nextFrame'] = "0"
        self.variable['_seqInfo.framesLeft'] = "0"

    async def on_ScreenprocessSequence_273(self):
        if self.variable['_seqInfo.running'] == "false":
            control_stop
        event_broadcastandwait
        if self.variable['Return value'] < self.variable['_seqInfo.nextFrame']:
            control_stop
        self.variable['_seqInfo.nextFrame'] += 60
        procedures_call

    async def on_ScreenpaintBox_274(self):
        self.lists['Params'].append("Screen.paintBox")
        event_broadcastandwait

    async def on_ScreenshowGrid_275(self):
        self.lists['Params'].append("Screen.showGrid: Shouldn't call this as it serves no purpose")
        event_broadcastandwait

    async def on_Scratchinitialise_276(self):
        procedures_call

    async def on_ScreensequenceRunning_277(self):
        self.variable['Return value'] = self.variable['_seqInfo.running']

    async def on_deleteScreen_278(self):
        self.lists['Params'].append("delete Screen")
        event_broadcastandwait

    async def on_ScreenseqFramesLeft_279(self):
        self.variable['Return value'] = self.variable['_seqInfo.framesLeft']

    async def on_Scratchreset_280(self):
        self.lists['_seqGrid'] = []
        self.variable['_seqInfo.seqData'] = ""
        if sensing_of == "true":
            data_showvariable
            data_showlist
            await asyncio.sleep(0)
        data_hidevariable
        data_hidelist

    async def on_ScreenforceRefresh_281(self):
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("Screen.forceRefresh - shouldn't call this as it serves no purpose!")
            event_broadcastandwait

    async def on_blitbackground_282(self):
        pen_clear
        self.size = self.variable['Scale'] * 100
        if not self.variable['_blit.backdrop'] == "-1":
            self.switch_costume(self.variable['_blit.backdrop'] + "")
            if not self.current_costume == self.variable['_blit.backdrop']:
                self.lists['Params'].append("_blitBackground: costume " + self.variable['_blit.backdrop'] + " not found")
                event_broadcastandwait
            self.xpos = 0
            self.ypos = 36
            pen_stamp

    async def on_blitgrid_283(self):
        procedures_call

    async def on_blitbackgroundMask_284(self):
        if not self.variable['_blit.backdrop'] == "-1":
            self.variable['bgMask'] = self.variable['_blit.backdrop'] + "_mask"
            self.switch_costume(self.variable['bgMask'] + "")
            if self.current_costume == self.variable['bgMask']:
                self.xpos = 0
                self.ypos = 36
                pen_stamp
            self.variable['_blit.backdrop'] = "-1"


class skysky(SpriteBase):
    async def on_SkyEngineinit_285(self):
        event_broadcastandwait
        self.lists['Params'].append("255")
        event_broadcastandwait
        event_broadcastandwait
        self.variable['_SystemVars.gameVersion'] = self.variable['Return value']
        event_broadcastandwait
        event_broadcastandwait
        if self.variable['Return value'] == "true":
            self.variable['_systemVars.systemFlags'] += self.variable['SF_ALLOW_TEXT'] + self.variable['SF_ALLOW_SPEECH']
        else:
            self.variable['_systemVars.systemFlags'] += self.variable['SF_ALLOW_TEXT']
        self.variable['_systemVars.systemFlags'] += self.variable['SF_PLAY_VOCS']
        self.variable['_SystemVars.gameSpeed'] = "80"
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        self.variable['_SystemVars.language'] = self.variable['SKY_ENGLISH']

    async def on_Scratchinitialise_286(self):
        self.variable['TOP_LEFT_Y'] = "132"
        self.variable['SKY_ENGLISH'] = "0"
        self.variable['SF_FX_OFF'] = operator_round
        self.variable['SF_MUS_OFF'] = operator_round
        self.variable['SF_CHOOSING'] = operator_round
        self.variable['SF_NO_SCROLL'] = operator_round
        self.variable['SF_GAME_RESTORED'] = operator_round
        self.variable['SF_PLAY_VOCS'] = operator_round
        self.variable['SF_ALLOW_SPEECH'] = operator_round
        self.variable['SF_ALLOW_TEXT'] = operator_round
        self.variable['SF_MOUSE_LOCKED'] = operator_round
        self.variable['_SystemVars.gameVersion'] = "0"
        self.variable['_SystemVars.mouseFlag'] = "0"
        self.variable['_SystemVars.language'] = "0"
        self.variable['_SystemVars.currentPalette'] = "4316"
        self.variable['_SystemVars.gameSpeed'] = "0"
        self.variable['_SystemVars.currentMusic'] = "0"
        self.variable['_SystemVars.pastIntro'] = "false"
        self.variable['_SystemVars.paused'] = "false"
        self.variable['_systemVars.systemFlags'] = "0"
        self.variable['keyDown?'] = "true"

    async def on_SkyEngineisDemo_287(self):
        self.variable['Return value'] = "false"

    async def on_SkyEngineisCDVersion_288(self):
        self.variable['Return value'] = "false"

    async def on_newSkyEngine_289(self):
        self.variable['_fastMode'] = "false"

    async def on_SkyEnginego_290(self):
        self.lists['Params'].append("1")
        self.lists['Params'].append("SkyEngine.go")
        event_broadcastandwait
        self.lists['Params'].append("2")
        self.lists['Params'].append("Logic.engine")
        event_broadcastandwait
        self.lists['Params'].append("3")
        self.lists['Params'].append("Screen.spriteEngine")
        event_broadcastandwait
        self.variable['result'] = "0"
        if not self.variable['result'] == "106":
            if CONDITION:
                self.variable['introSkipped'] = "false"
                if self.variable['_SystemVars.gameVersion'] > "272":
                    event_broadcastandwait
                    self.variable['floppyIntro'] = "false"
                    self.lists['Params'].append(self.variable['floppyIntro'])
                    event_broadcastandwait
                    self.variable['introSkipped'] = not self.variable['Return value'] == "true"
                    event_broadcastandwait
            else:
                self.variable['introSkipped'] = sensing_of == "tickbox"
            self.lists['Params'].append("true")
            event_broadcastandwait
            if self.variable['introSkipped'] == "true":
                event_broadcastandwait
                event_broadcast
            else:
                event_broadcastandwait
        event_broadcastandwait
        self.variable['delayCount'] = self.variable['Return value']
        while True:
            if self.variable['Debug.Timers?'] == "true":
                self.lists['Params'].append("1")
                event_broadcastandwait
            if self.variable['Debug.Timers?'] == "true":
                self.lists['Params'].append("2")
                event_broadcastandwait
            event_broadcastandwait
            event_broadcastandwait
            procedures_call
            if self.variable['_SystemVars.paused'] == "true":
                self.lists['Params'].append("SkyEngine.go: paused functionality")
                event_broadcastandwait
            event_broadcastandwait
            event_broadcastandwait
            event_broadcastandwait
            event_broadcastandwait
            if self.variable['Toolbar.run?'] == "true":
                procedures_call
            else:
                self.variable['delayCount'] += self.variable['_SystemVars.gameSpeed']
                event_broadcastandwait
                self.variable['needDelay'] = self.variable['delayCount'] - self.variable['Return value']
                if self.variable['needDelay'] < "0" or self.variable['needDelay'] > self.variable['_SystemVars.gameSpeed']:
                    self.variable['needDelay'] = "0"
                    self.variable['delayCount'] = self.variable['Return value']
                procedures_call
            if self.variable['Debug.Timers?'] == "true":
                self.lists['Params'].append("2")
                event_broadcastandwait
            self.lists['Params'].append("true")
            event_broadcastandwait
            if self.variable['Debug.Timers?'] == "true":
                self.lists['Params'].append("1")
                event_broadcastandwait
            if self.variable['Debug.Fps?'] == "true":
                event_broadcastandwait

    async def on_SkyEngineinitItemList_291(self):
        self.lists['SkyEngine._ItemList'] = []
        for _ in range(300):
            self.lists['SkyEngine._ItemList'].append("0")

    async def on_SkyEngineloadFixedItems_292(self):
        self.lists['Params'].append("36")
        event_broadcastandwait
        self.lists['SkyEngine._ItemList'][37] = self.variable['Return value']
        self.variable['i'] = "49"
        for _ in range(2):
            self.lists['Params'].append(self.variable['i'])
            event_broadcastandwait
            self.lists['SkyEngine._ItemList'][self.variable['i'] + 1] = self.variable['Return value']
            self.variable['i'] += 1
        self.lists['Params'].append("73")
        event_broadcastandwait
        self.lists['SkyEngine._ItemList'][74] = self.variable['Return value']
        self.variable['i'] = "262"
        for _ in range(6):
            self.lists['Params'].append(self.variable['i'])
            event_broadcastandwait
            self.lists['SkyEngine._ItemList'][self.variable['i'] + 1] = self.variable['Return value']
            self.variable['i'] += 1
        self.lists['Params'].append("269")
        event_broadcastandwait
        self.lists['SkyEngine._ItemList'][270] = self.variable['Return value']
        self.variable['i'] = "271"
        for _ in range(2):
            self.lists['Params'].append(self.variable['i'])
            event_broadcastandwait
            self.lists['SkyEngine._ItemList'][self.variable['i'] + 1] = self.variable['Return value']
            self.variable['i'] += 1

    async def on_SkyEnginefetchItem_293(self):
        self.variable['num'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = self.lists['SkyEngine._ItemList'][self.variable['num'] + 1]

    async def on_Scratchreset_294(self):
        self.lists['SkyEngine._ItemList'] = []
        if sensing_of == "true":
            data_showlist
            await asyncio.sleep(0)
        data_hidelist


class skysound(SpriteBase):
    async def on_newSound_295(self):
        self.lists['Sound._SaveSounds'][1] = "65535"
        self.lists['Sound._SaveSounds'][2] = "65535"
        self.variable['_mainSfxVolume'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['_isPaused'] = "false"

    async def on_SoundplaySounduintuintuint_296(self):
        self.variable['channel'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['volume'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['sound'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call

    async def on_SoundloadSection_297(self):
        self.variable['pSection'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        event_broadcastandwait

    async def on_SoundplaySounduintbyteuintSoundHandle_298(self):
        self.lists['Params'].append("Sound.playSound (uint32, byte*, uint32, SoundHandle*): Shouldn't be getting called at all")
        event_broadcastandwait

    async def on_SoundfnStartFx_299(self):
        self.variable['channel'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['sound'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Sound._SaveSounds'][self.variable['channel'] + 1] = "0"
        self.variable['screen'] = self.lists['Logic._ScriptVariables'][sensing_of] % 256
        if self.variable['sound'] == "278" and self.variable['screen'] == "25":
            self.variable['sound'] = "394"
        if self.variable['sound'] % 512 > "255":
            self.variable['sound'] += -256
        self.variable['sfx'] = self.variable['sound'] * 32 + 1
        self.variable['roomList'] = self.variable['sfx'] + 2
        self.variable['i'] = "0"
        if not self.lists['musicList'][self.variable['roomList'] + self.variable['i']] == "255":
            while not self.lists['musicList'][self.variable['roomList'] + self.variable['i']] == self.variable['screen']:
                self.variable['i'] += 3
                if self.lists['musicList'][self.variable['roomList'] + self.variable['i']] == "255":
                    control_stop
        self.variable['volume'] = operator_mathop
        if self.lists['musicList'][self.variable['sfx'] + 1] > "127":
            self.lists['_sfxQueue'].append(self.variable['channel'])
            self.lists['_sfxQueue'].append(self.lists['musicList'][self.variable['sfx']])
            self.lists['_sfxQueue'].append(self.variable['volume'])
            self.lists['_sfxQueue'].append(self.lists['musicList'][self.variable['sfx'] + 1] % 256)
            control_stop
        if self.lists['musicList'][self.variable['sfx'] + 1] % 64 > "31":
            self.lists['Sound._SaveSounds'][self.variable['channel'] + 1] = self.lists['musicList'][self.variable['sfx']] + self.variable['volume'] * 256
        procedures_call

    async def on_SoundcheckFxQueue_300(self):
        self.variable['cnt'] = "1"
        while not self.variable['cnt'] > len(self.lists['_sfxQueue']):
            if not self.lists['_sfxQueue'][self.variable['cnt'] + 3] == "0":
                self.lists['_sfxQueue'][self.variable['cnt'] + 3] = self.lists['_sfxQueue'][self.variable['cnt'] + 3] - 1
                if self.lists['_sfxQueue'][self.variable['cnt'] + 3] == "0":
                    procedures_call
                    self.lists['_sfxQueue'].pop(self.variable['cnt'])
                    self.lists['_sfxQueue'].pop(self.variable['cnt'])
                    self.lists['_sfxQueue'].pop(self.variable['cnt'])
                    self.lists['_sfxQueue'].pop(self.variable['cnt'])
                    self.variable['cnt'] += -4
            self.variable['cnt'] += 4

    async def on_SoundrestoreSfx_301(self):
        self.lists['_sfxQueue'] = []
        if not self.lists['Sound._SaveSounds'][1] == "65535":
            self.lists['_sfxQueue'].append(self.lists['Sound._SaveSounds'][1] % 256)
            self.lists['_sfxQueue'].append(operator_mathop)
            self.lists['_sfxQueue'].append("0")
            self.lists['_sfxQueue'].append("1")
        if not self.lists['Sound._SaveSounds'][2] == "65535":
            self.lists['_sfxQueue'].append(self.lists['Sound._SaveSounds'][2] % 256)
            self.lists['_sfxQueue'].append(operator_mathop)
            self.lists['_sfxQueue'].append("1")
            self.lists['_sfxQueue'].append("1")

    async def on_SoundfnStopFx_302(self):
        self.lists['Sound control'].append("Stop")
        self.lists['Sound control'].append("0")
        self.lists['Sound control'].append("Stop")
        self.lists['Sound control'].append("1")
        self.lists['Sound._SaveSounds'][1] = "65535"
        self.lists['Sound._SaveSounds'][2] = "65535"

    async def on_SoundstopSpeech_303(self):
        self.lists['Params'].append("Sound.stopSpeech")
        event_broadcastandwait

    async def on_SoundstartSpeech_304(self):
        self.lists['Params'].append("Sound.startSpeech")
        event_broadcastandwait

    async def on_SoundfnPauseFx_305(self):
        if self.variable['_isPaused'] == "false":
            self.variable['_isPaused'] = "true"
            self.lists['Sound control'].append("Pause")
            self.lists['Sound control'].append("0")
            self.lists['Sound control'].append("Pause")
            self.lists['Sound control'].append("1")

    async def on_SoundfnUnPauseFx_306(self):
        if self.variable['_isPaused'] == "true":
            self.variable['_isPaused'] = "false"
            self.lists['Sound control'].append("Unpause")
            self.lists['Sound control'].append("0")
            self.lists['Sound control'].append("Unpause")
            self.lists['Sound control'].append("1")

    async def on_initialisesound_307(self):
        event_broadcastandwait
        procedures_call

    async def on_Scratchreset_308(self):
        self.lists['Sound._SaveSounds'] = []
        self.lists['_sfxQueue'] = []
        self.lists['musicList'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist


class skysprites(SpriteBase):
    async def on_ScreenspriteEngine_309(self):
        self.lists['_blit.backSprites'] = []
        self.lists['_blit.frontSprites'] = []
        if self.variable['Debug?'] == "false":
            procedures_call
            procedures_call
            procedures_call
        else:
            self.lists['Params'].append("doSprites(0)")
            event_broadcastandwait
            procedures_call
            self.lists['Params'].append("sortSprites()")
            event_broadcastandwait
            procedures_call
            self.lists['Params'].append("doSprites(1)")
            event_broadcastandwait
            procedures_call
            self.lists['Params'].append("end SpriteEngine")
            event_broadcastandwait
            self.lists['Params'].append("")
            event_broadcastandwait

    async def on_Scratchreset_310(self):
        self.lists['sortList.sprite'] = []
        self.lists['sortList.spriteComp'] = []
        self.lists['sortList.yCood'] = []
        self.lists['_blit.backSprites'] = []
        self.lists['_blit.frontSprites'] = []
        self.lists['Sprites.data'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist

    async def on_Scratchinitialise_311(self):
        self.visible = 0
        procedures_call

    async def on_blitbackSprites_312(self):
        procedures_call

    async def on_debug_313(self):
        if self.variable['Debug?'] == "true":
            self.lists['Params'].append("3")
            event_broadcastandwait
            self.lists['Params'].append("costume# " + operator_mathop)
            event_broadcastandwait

    async def on_blitfrontSprites_314(self):
        procedures_call


class skytext(SpriteBase):
    async def on_newText_315(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.lists['Params'].append("60150")
        event_broadcastandwait
        self.variable['_mainCharacterSet.addr'] = self.variable['Return value']
        self.variable['_mainCharacterSet.charHeight'] = "12"
        self.variable['_mainCharacterSet.charSpacing'] = "0"
        self.lists['Params'].append("0")
        event_broadcastandwait
        self.lists['Params'].append("60520")
        event_broadcastandwait
        self.variable['_controlCharacterSet.addr'] = self.variable['Return value']
        self.variable['_controlCharacterSet.charHeight'] = "12"
        self.variable['_controlCharacterset.charSpacing'] = "0"
        self.lists['Params'].append("60521")
        event_broadcastandwait
        self.variable['_linkCharacterSet.addr'] = self.variable['Return value']
        self.variable['_linkCharacterSet.charHeight'] = "12"
        self.variable['_linkCharacterSet.charSpacing'] = "1"

    async def on_TextfnSetFont_316(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['fontNr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        if self.variable['fontNr'] == "0":
            self.variable['_characterSet'] = self.variable['_mainCharacterSet.addr']
            self.variable['_charHeight'] = self.variable['_mainCharacterSet.charHeight']
            self.variable['_dtCharSpacing'] = self.variable['_mainCharacterSet.charSpacing']
            self.variable['textFile'] = "60150"
        else:
            if self.variable['fontNr'] == "1":
                self.variable['_characterSet'] = self.variable['_linkCharacterSet.addr']
                self.variable['_charHeight'] = self.variable['_linkCharacterSet.charHeight']
                self.variable['_dtCharSpacing'] = self.variable['_linkCharacterSet.charSpacing']
                self.variable['textFile'] = "60521"
            else:
                self.variable['_characterSet'] = self.variable['_controlCharacterSet.addr']
                self.variable['_charHeight'] = self.variable['_controlCharacterSet.charHeight']
                self.variable['_dtCharSpacing'] = self.variable['_controlCharacterset.charSpacing']
                self.variable['textFile'] = "60520"
        self.variable['_curCharSet'] = self.variable['fontNr']

    async def on_TextfnTextModule_317(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['textNo'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['textInfoId'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append("1")
        event_broadcastandwait
        self.lists['Params'].append(self.variable['textInfoId'])
        event_broadcastandwait
        self.variable['msgData'] = self.variable['Return value']
        procedures_call
        self.lists['Logic._ScriptVariables'][sensing_of] = self.variable['textId.compactNum']
        self.lists['Params'].append(self.variable['textId.compactNum'])
        event_broadcastandwait
        self.variable['textCompact'] = self.variable['Return value']
        self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 6] = self.lists['SkyCompact._RawBuff'][self.variable['msgData'] + 3]
        self.lists['SkyCompact._RawBuff'][self.variable['textCompact'] + 7] = self.lists['SkyCompact._RawBuff'][self.variable['msgData'] + 4]
        self.lists['Params'].append("0")
        event_broadcastandwait

    async def on_TextfnPointerText_318(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['mouseY'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['mouseX'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['pointedId'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append(self.variable['pointedId'])
        event_broadcastandwait
        self.variable['ptrComp'] = self.variable['Return value']
        procedures_call
        self.variable['text'] = self.variable['Return value']
        self.lists['Logic._ScriptVariables'][sensing_of] = self.lists['displayedText.compactNum'][self.variable['Return value']]
        if not self.lists['Logic._ScriptVariables'][sensing_of] == "0":
            self.variable['mouseOfsY'] = self.variable['TOP_LEFT_Y'] - 2
            if self.variable['mouseX'] < "150":
                self.variable['mouseOfsX'] = "10"
            else:
                self.variable['mouseOfsX'] = -10 - self.lists['displayedText.textWidth'][self.variable['Return value']]
        else:
            self.variable['mouseOfsY'] = self.variable['TOP_LEFT_Y'] - 16
            if self.variable['mouseX'] < "150":
                self.variable['mouseOfsX'] = "5"
            else:
                self.variable['mouseOfsX'] = -5 - self.lists['displayedText.textWidth'][self.variable['Return value']]
        self.lists['Params'].append(self.variable['mouseX'] + self.variable['mouseOfsX'])
        if self.variable['mouseY'] + self.variable['mouseOfsY'] < self.variable['TOP_LEFT_Y']:
            self.lists['Params'].append(self.variable['TOP_LEFT_Y'] - 128)
        else:
            self.lists['Params'].append(self.variable['mouseY'] + self.variable['mouseOfsY'] - 128)
        self.variable['_pointerTextId'] = self.variable['Return value']
        self.lists['Params'].append(self.variable['Return value'])
        event_broadcastandwait

    async def on_TextlogicCursor_319(self):
        procedures_call
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['mouseY'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['mouseX'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['textCompact'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].append("Text.logicCursor")
        event_broadcastandwait

    async def on_TextdisplayTextuintuintbooluintuint_320(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['color'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['pixelWidth'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['center'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['textNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call
        procedures_call

    async def on_TextdisplayTextcharuintbooluintuint_321(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['color'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['pixelWidth'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['center'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['textPtr'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call

    async def on_TextchangeTextSpriteColor_322(self):
        if self.variable['clone?'] == "false":
            event_broadcastandwait
            self.lists['Params'].pop(len(self.lists['Params']))
            self.lists['Params'].pop(len(self.lists['Params']))

    async def on_TextgiveCurrentCharSet_323(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.lists['Params'].append("Text.giveCurrentCharSet")
        event_broadcastandwait

    async def on_Scratchreset_324(self):
        self.lists['_textBuffer'] = []
        self.lists['_huffTree.lChild'] = []
        self.lists['_huffTree.rChild'] = []
        self.lists['_huffTree.value'] = []
        self.lists['centerTable'] = []
        self.lists['_textIdSlot'] = []
        self.lists['displayedText.compactNum'] = []
        self.lists['displayedText.textData'] = []
        self.lists['displayedText.textWidth'] = []
        self.lists['_dest'] = []
        self.lists['displayText.textDataLength'] = []
        self.lists['bufferedBlit'] = []
        self.lists['Text._BufferedDestroy'] = []
        self.visible = 0
        control_delete_this_clone

    async def on_Scratchinitialise_325(self):
        self.variable['clone?'] = "false"
        for _ in range(1024):
            self.lists['_textBuffer'].append("0")
        for _ in range(10):
            self.lists['centerTable'].append("0")
        event_broadcastandwait
        self.variable['hex'] = self.variable['Return value']
        self.variable['i'] = "0"
        for _ in range(operator_length / 6):
            procedures_call
            self.variable['i'] += 1
            self.lists['_huffTree.lChild'].append(self.variable['Return value'])
            procedures_call
            self.variable['i'] += 1
            self.lists['_huffTree.rChild'].append(self.variable['Return value'])
            procedures_call
            self.variable['i'] += 1
            self.lists['_huffTree.value'].append(self.variable['Return value'])
        self.variable['hex'] = ""
        self.variable['_pointerTextId'] = "0"

    async def on_blittext_326(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.lists['bufferedBlit'].append(self.lists['_textIdSlot'][self.lists['Params'][len(self.lists['Params'])]])
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call

    async def on_TextlowTextManager_327(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['center'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['color'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['logicNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['width'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['textNum'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        procedures_call

    async def on_blitdestroyText_328(self):
        if self.variable['clone?'] == "false":
            self.lists['Text._BufferedDestroy'].append(self.lists['Params'][len(self.lists['Params'])])
            self.lists['Params'].pop(len(self.lists['Params']))
            event_broadcastandwait
            procedures_call

    async def clone_start2(self):
        self.variable['clone?'] = "true"
        self.visible = 1

    async def on_blitDestroyTextinternal_329(self):
        if self.variable['clone?'] == "true":
            if data_itemnumoflist > "0":
                control_delete_this_clone

    async def on_TextgetCompactNumFromId_330(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.variable['i'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = self.lists['displayedText.compactNum'][self.variable['i']]

    async def on_TextchangeTextSpriteColorinternal_331(self):
        if self.variable['clone?'] == "true":
            if self.variable['cloneId'] == self.lists['Params'][len(self.lists['Params']) - 1]:
                looks_seteffectto

    async def on_blitprepText_332(self):
        if self.variable['clone?'] == "true":
            control_stop
        self.lists['bufferedBlit'].append(self.lists['_textIdSlot'][self.lists['Params'][len(self.lists['Params'])]])
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))

    async def on_blitbufferedText_333(self):
        if self.variable['clone?'] == "true":
            control_stop
        procedures_call

    async def on_blitprepBufferedDestroy_334(self):
        if self.variable['clone?'] == "false":
            self.lists['Text._BufferedDestroy'].append(self.lists['Params'][len(self.lists['Params'])])
            self.lists['Params'].pop(len(self.lists['Params']))

    async def on_blitbufferedDestroy_335(self):
        if self.variable['clone?'] == "false":
            event_broadcastandwait
            procedures_call


class scratchmain(SpriteBase):
    async def green_flag1(self):
        self.variable['Debug?'] = "false"
        pen_clear
        self.switch_costume('thumbnail2')
        self.visible = 1
        self.variable['Scale'] = "1.5"
        event_broadcastandwait
        event_broadcastandwait
        self.variable['start clock'] = sensing_dayssince2000
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        event_broadcastandwait
        self.visible = 0
        event_broadcastandwait

    async def on_scratchgetMillis_336(self):
        self.variable['Return value'] = operator_round

    async def on_Scratchthumbnail_337(self):
        self.variable['doing thumbnail?'] = "true"
        event_broadcastandwait
        self.switch_costume('thumbnail')
        self.xpos = 0
        self.ypos = 0
        looks_gotofrontback
        self.visible = 1
        pen_clear
        self.variable['doing thumbnail?'] = "false"

    async def on_Scratchreset_338(self):
        self.lists['Generic list'] = []
        self.lists['Params'] = []
        if self.variable['doing thumbnail?'] == "true":
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist

    async def on_BitwiseOru_339(self):
        self.variable['num1'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['num2'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = "0"
        self.variable['addVal'] = "1"
        for _ in range(16):
            if self.variable['num1'] % 2 == "1" or self.variable['num2'] % 2 == "1":
                self.variable['Return value'] += self.variable['addVal']
            self.variable['num1'] = operator_mathop
            self.variable['num2'] = operator_mathop
            self.variable['addVal'] += self.variable['addVal']

    async def on_BitwiseXORu_340(self):
        self.variable['num1'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['num2'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = "0"
        self.variable['addVal'] = "1"
        for _ in range(16):
            if not self.variable['num1'] % 2 == self.variable['num2'] % 2:
                self.variable['Return value'] += self.variable['addVal']
            self.variable['num1'] = operator_mathop
            self.variable['num2'] = operator_mathop
            self.variable['addVal'] += self.variable['addVal']

    async def on_BitwiseAndu_341(self):
        self.variable['num1'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['num2'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = "0"
        self.variable['addVal'] = "1"
        for _ in range(16):
            if self.variable['num1'] % 2 == "1" and self.variable['num2'] % 2 == "1":
                self.variable['Return value'] += self.variable['addVal']
            self.variable['num1'] = operator_mathop
            self.variable['num2'] = operator_mathop
            self.variable['addVal'] += self.variable['addVal']

    async def on_SkyEnginedeinitVirgin_342(self):
        self.visible = 0


class scratchfader(SpriteBase):
    async def on_initialisefader_343(self):
        event_broadcastandwait
        self.variable['clone?'] = "false"
        self.variable['alpha'] = "0"
        self.xpos = 0
        self.ypos = 0
        self.switch_costume('white')
        looks_seteffectto
        looks_seteffectto
        self.visible = 1
        looks_gotofrontback
        event_broadcastandwait

    async def on_ScratchFaderfadeUp_344(self):
        if self.variable['clone?'] == "false":
            while not self.variable['alpha'] == "100":
                self.variable['alpha'] += 10
                looks_seteffectto

    async def on_ScratchFaderfadeDown_345(self):
        if self.variable['clone?'] == "false":
            while not self.variable['alpha'] == "0":
                self.variable['alpha'] += -10
                looks_seteffectto

    async def clone_start3(self):
        self.variable['clone?'] = "true"
        looks_cleargraphiceffects
        self.switch_costume('border')

    async def on_changescale_346(self):
        self.size = self.variable['Scale'] * 100

    async def on_Scratchinitialise_347(self):
        self.visible = 0

    async def on_ScratchFaderpauseAndFadeUp_348(self):
        if self.variable['clone?'] == "false":
            await asyncio.sleep(0.2)
            event_broadcastandwait

    async def on_Scratchreset_349(self):
        self.visible = 0


class scratchsfx(SpriteBase):
    async def on_Scratchreset_350(self):
        self.lists['Sound control'] = []
        self.lists['sounds'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist

    async def on_Scratchinitialise_351(self):
        self.variable['clone?'] = "false"
        self.lists['sounds'].append("s0-fx1-l")
        self.lists['sounds'].append("s0-fx2")
        self.lists['sounds'].append("s1-fx3")
        self.lists['sounds'].append("s1-fx4")
        self.lists['sounds'].append("s1-fx4-l")
        self.lists['sounds'].append("s1-fx5")
        self.lists['sounds'].append("s1-fx6")
        self.lists['sounds'].append("s1-fx7")
        self.lists['sounds'].append("s1-fx7-l")
        self.lists['sounds'].append("s1-fx8-l")
        self.lists['sounds'].append("s1-fx9")
        self.lists['sounds'].append("s1-fx10")
        self.lists['sounds'].append("s1-fx11")
        self.lists['sounds'].append("s1-fx11-l")
        self.lists['sounds'].append("s1-fx12")
        self.lists['sounds'].append("s1-fx13")
        self.lists['sounds'].append("s1-fx14")
        self.lists['sounds'].append("s1-fx17-l")
        self.lists['sounds'].append("s1-fx18")
        self.lists['sounds'].append("s1-fx19")
        self.lists['sounds'].append("s1-fx26")
        self.variable['isPlaying?'] = "false"
        self.variable['channel'] = "0"
        control_create_clone_of
        self.variable['channel'] = "1"
        control_create_clone_of

    async def clone_start4(self):
        self.variable['clone?'] = "true"
        while True:
            while not len(self.lists['Sound control']) == "0":
                self.variable['command'] = self.lists['Sound control'][1]
                if self.variable['command'] == "Play":
                    if self.lists['Sound control'][2] == self.variable['channel']:
                        if self.variable['isPlaying?'] == "true":
                            self.variable['isPlaying?'] = "false"
                            control_create_clone_of
                            control_delete_this_clone
                else:
                    if self.variable['command'] == "Stop":
                        if self.lists['Sound control'][2] == self.variable['channel']:
                            self.lists['Sound control'].pop(1)
                            self.lists['Sound control'].pop(1)
                            if self.variable['isPlaying?'] == "true":
                                self.variable['isPlaying?'] = "false"
                                control_create_clone_of
                                control_delete_this_clone
                    else:
                        if self.variable['command'] == "Pause":
                            if self.lists['Sound control'][2] == self.variable['channel']:
                                self.lists['Sound control'].pop(1)
                                self.lists['Sound control'].pop(1)
                                sound_setvolumeto
                        else:
                            if self.variable['command'] == "Unpause":
                                if self.lists['Sound control'][2] == self.variable['channel']:
                                    self.lists['Sound control'].pop(1)
                                    self.lists['Sound control'].pop(1)
                                    sound_setvolumeto
                            else:
                                SUBSTACK2

    async def clone_start5(self):
        while True:
            while not len(self.lists['Sound control']) == "0":
                self.variable['command'] = self.lists['Sound control'][1]
                if self.variable['command'] == "Play":
                    if self.lists['Sound control'][2] == self.variable['channel']:
                        if self.variable['isPlaying?'] == "false":
                            self.variable['volume'] = self.lists['Sound control'][3] * 100 / 255
                            self.variable['name'] = self.lists['Sound control'][4]
                            if self.variable['Debug?'] == "true":
                                if not data_itemnumoflist > "0" or data_itemnumoflist > "0":
                                    self.lists['Params'].append("Missing sfx: " + self.variable['name'])
                                    event_broadcastandwait
                            self.variable['isPlaying?'] = "true"
                            self.lists['Sound control'].pop(1)
                            self.lists['Sound control'].pop(1)
                            self.lists['Sound control'].pop(1)
                            self.lists['Sound control'].pop(1)
                            sound_setvolumeto
                            if data_itemnumoflist > "0":
                                sound_playuntildone
                            if data_itemnumoflist > "0":
                                while True:
                                    sound_playuntildone
                            self.variable['isPlaying?'] = "false"
                else:
                    SUBSTACK2

    async def on_FxsetEnabled_352(self):
        if self.variable['clone?'] == "true":
            sound_setvolumeto


class data(SpriteBase):
    async def on_DatagetCompactDataFile_353(self):
        self.variable['Return value'] = self.variable['compactDataFile']

    async def on_DataconvertGenericUListToReturnValue_354(self):
        self.variable['Return value'] = ""
        self.variable['i'] = "1"
        for _ in range(len(self.lists['Generic list'])):
            self.variable['u16'] = self.lists['Generic list'][self.variable['i']]
            self.variable['byte'] = self.variable['u16'] % 256
            self.variable['Return value'] = self.variable['Return value'] + self.lists['Hex'][operator_mathop + 1]
            self.variable['Return value'] = self.variable['Return value'] + self.lists['Hex'][self.variable['byte'] % 16 + 1]
            self.variable['byte'] = operator_mathop
            self.variable['Return value'] = self.variable['Return value'] + self.lists['Hex'][operator_mathop + 1]
            self.variable['Return value'] = self.variable['Return value'] + self.lists['Hex'][self.variable['byte'] % 16 + 1]
            self.variable['i'] += 1
        self.lists['Generic list'] = []

    async def on_Scratchreset_355(self):
        self.lists['fileData'] = []
        if sensing_of == "true":
            data_showlist
            await asyncio.sleep(0)
        data_hidelist

    async def on_Scratchinitialise_356(self):
        procedures_call

    async def on_DataloadFile_357(self):
        self.variable['i'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['Return value'] = self.lists['fileData'][self.variable['i']]

    async def on_DatagetScriptVariables_358(self):
        self.variable['Return value'] = self.variable['scriptVariables']

    async def on_DatagetCompactOffsets_359(self):
        self.variable['Return value'] = self.variable['compactOffsets']

    async def on_DatagetMegaSetOffsets_360(self):
        self.variable['Return value'] = self.variable['megaSetOffsets']

    async def on_DatagetTurnTableOffsets_361(self):
        self.variable['Return value'] = self.variable['turnTableOffsets']

    async def on_DatagetGameGrids_362(self):
        self.variable['Return value'] = self.variable['gameGrids']

    async def on_DatagetGridConvertTable_363(self):
        self.variable['Return value'] = self.variable['gridConvertTable']

    async def on_DatagetHuffData_364(self):
        self.variable['Return value'] = self.variable['huffData']

    async def on_DatagetMusicListData_365(self):
        self.variable['Return value'] = self.variable['musicListData']


class debug(SpriteBase):
    async def on_scratchwarning_366(self):
        if data_itemnumoflist == "0":
            self.lists['Warnings'].append(self.lists['Params'][len(self.lists['Params'])])
        event_broadcastandwait

    async def on_scratcherror_367(self):
        if data_itemnumoflist == "0":
            self.lists['Errors'].append(self.lists['Params'][len(self.lists['Params'])])
        event_broadcastandwait

    async def on_Scratchreset_368(self):
        self.lists['Warnings'] = []
        self.lists['Errors'] = []
        self.lists['Debug log'] = []
        self.lists['Sprite files'] = []
        self.lists['Graphics log'] = []
        self.lists['fps'] = []
        self.lists['allOptimisationTimers'] = []
        self.lists['Debug.optimisationTimer'] = []
        self.lists['optimisationTimerName'] = []
        self.lists['Debug.timers'] = []
        if sensing_of == "true":
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            data_showlist
            await asyncio.sleep(0)
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidelist
        data_hidevariable

    async def on_Debuglogic_369(self):
        self.variable['logic'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Debug log'].append("LOGIC: " + self.lists['logic_table_names'][self.variable['logic'] + 1])

    async def on_Debugscript_370(self):
        self.lists['Generic list'] = []
        self.lists['Generic list'].append(self.lists['Params'][len(self.lists['Params']) - 2])
        self.lists['Generic list'].append(self.lists['Params'][len(self.lists['Params']) - 1])
        self.lists['Generic list'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['command'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Debug log'].append("SCRIPT: " + self.lists['opcodes'][self.variable['command'] + 1])
        if self.variable['command'] == "0" or self.variable['command'] == "6":
            self.lists['Debug log'].append(" " + self.lists['scriptVars'][self.lists['Generic list'][1] / 4 + 1])
        else:
            self.variable['i'] = "1"
            for _ in range(self.lists['opcode_par'][self.variable['command'] + 1]):
                self.lists['Debug log'].append(" " + self.lists['Generic list'][self.variable['i']])
                self.variable['i'] += 1
        self.lists['Debug log'].append("")

    async def on_Debugmcode_371(self):
        self.variable['c'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['b'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['a'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['mcode'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Debug log'].append("MCODE: " + self.lists['mcodes'][self.variable['mcode'] + 1] + "(" + self.variable['a'] + ", " + self.variable['b'] + ", " + self.variable['c'] + ")")

    async def on_Debugdebug_372(self):
        self.variable['string'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Debug log'].append(self.variable['string'])

    async def on_DebugspriteFiles_373(self):
        if data_itemnumoflist == "0":
            self.lists['Sprite files'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))

    async def on_scratchgraphicslog_374(self):
        self.lists['Graphics log'].append(self.lists['Params'][len(self.lists['Params'])])
        self.lists['Params'].pop(len(self.lists['Params']))

    async def on_framecounter_375(self):
        if self.variable['Debug.Fps?'] == "true":
            procedures_call
        if self.variable['Debug?'] == "true":
            if self.variable['Debug.Timers?'] == "true":
                procedures_call

    async def on_initialisedebug_376(self):
        if self.variable['Debug?'] == "true":
            event_broadcastandwait
        self.variable['Debug.Fps?'] = "false"
        self.variable['Debug.Timers?'] = "false"
        self.variable['Debug.Grid?'] = "false"

    async def on_optimisationstartTimerN_377(self):
        self.variable['i'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Debug.optimisationTimer'][self.variable['i'] * 2] = sensing_dayssince2000

    async def on_optimisationstopTimerN_378(self):
        self.variable['i'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['Debug.optimisationTimer'][self.variable['i'] * 2 - 1] = self.lists['Debug.optimisationTimer'][self.variable['i'] * 2 - 1] + sensing_dayssince2000 - self.lists['Debug.optimisationTimer'][self.variable['i'] * 2]

    async def on_optimisationTimersetNameN_379(self):
        self.variable['name'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.variable['i'] = self.lists['Params'][len(self.lists['Params'])]
        self.lists['Params'].pop(len(self.lists['Params']))
        self.lists['optimisationTimerName'][self.variable['i']] = self.variable['name']

    async def on_optimisationinitialise_380(self):
        procedures_call


class logo(SpriteBase):
    async def on_SkyEngineinitVirgin_381(self):
        self.switch_costume('logo')
        self.xpos = 0
        self.ypos = 0
        looks_seteffectto
        looks_gotofrontback
        looks_goforwardbackwardlayers
        self.visible = 1
        control_create_clone_of
        for _ in range(10):
            looks_changeeffectby
            await asyncio.sleep(0.05)

    async def on_Scratchinitialise_382(self):
        self.visible = 0
        self.variable['clone?'] = "false"
        control_delete_this_clone

    async def on_SkyEnginedeinitVirgin_383(self):
        if self.variable['clone?'] == "true":
            looks_gotofrontback
            for _ in range(10):
                looks_changeeffectby
            event_broadcastandwait
            pen_clear
            control_delete_this_clone

    async def clone_start6(self):
        self.variable['clone?'] = "true"
        self.switch_costume('black')

    async def on_hidelogo_384(self):
        if self.variable['clone?'] == "false":
            self.visible = 0


class skip(SpriteBase):
    async def on_Scratchinitialise_385(self):
        looks_gotofrontback
        self.xpos = 0
        self.ypos = 0
        self.visible = 1
        self.switch_costume('crossbox')

    async def on_hidelogo_386(self):
        self.visible = 0

    async def on_Scratchreset_387(self):
        self.visible = 0


class toolbar(SpriteBase):
    async def on_initialisetoolbar_388(self):
        looks_gotofrontback
        self.visible = 1
        self.ypos = -144
        self.xpos = -207
        self.variable['state?'] = "false"
        self.variable['cloneId'] = "use"
        control_create_clone_of
        self.xpos = -133
        self.switch_costume('load')
        self.variable['state?'] = "false"
        self.variable['cloneId'] = "load"
        control_create_clone_of
        self.xpos = -75
        self.switch_costume('save')
        self.variable['state?'] = "false"
        self.variable['cloneId'] = "save"
        control_create_clone_of
        self.xpos = 0
        self.variable['state?'] = "true"
        self.variable['cloneId'] = "sound"
        control_create_clone_of
        self.xpos = 58
        self.variable['state?'] = "true"
        self.variable['cloneId'] = "music"
        control_create_clone_of
        self.xpos = 133
        self.variable['state?'] = "false"
        self.variable['cloneId'] = "run"
        control_create_clone_of
        self.xpos = 207
        self.switch_costume('help')
        self.variable['state?'] = "false"
        self.variable['cloneId'] = "help"
        control_create_clone_of
        self.variable['cloneId'] = "master"
        self.visible = 0
        event_broadcastandwait

    async def on_Scratchreset_389(self):
        self.visible = 0
        control_delete_this_clone

    async def on_ToolbarupdateToolbar_390(self):
        procedures_call

    async def clone_start7(self):
        self.variable['newState?'] = self.variable['state?']
        self.variable['state?'] = not self.variable['state?'] == "true"


class info(SpriteBase):
    async def on_Infoshow_391(self):
        self.variable['clone?'] = "false"
        self.xpos = 210
        self.ypos = -150
        self.switch_costume('forward')
        self.visible = 1
        self.variable['Info.Page'] = "1"
        control_create_clone_of
        while not self.variable['Info.Page'] > "6":
            await asyncio.sleep(0)
        self.visible = 0

    async def clone_start8(self):
        self.variable['clone?'] = "true"
        self.xpos = 0
        self.ypos = 0
        self.switch_costume('page 1')
        self.variable['page'] = "1"
        while not self.variable['Info.Page'] > "6":
            while not self.variable['Info.Page'] > self.variable['page']:
                await asyncio.sleep(0)
            self.current_costume += 1
            if self.current_costume > len(self.costumes):
                self.current_costume = 0
            self.variable['page'] = self.variable['Info.Page']
        control_delete_this_clone

    async def on_Scratchreset_392(self):
        self.visible = 0
        control_delete_this_clone


class textbackground(SpriteBase):
    async def on_textstippleBackground_393(self):
        self.size = self.variable['Scale'] * 200
        self.xpos = 0
        self.ypos = 36 + 142 - self.lists['Params'][len(self.lists['Params'])] * 12 * self.variable['Scale']
        self.size = self.variable['Scale'] * 100
        self.lists['Params'].pop(len(self.lists['Params']))
        looks_gotofrontback
        self.visible = 1

    async def on_Scratchreset_394(self):
        self.visible = 0

    async def on_texthideBackground_395(self):
        self.visible = 0


class notes(SpriteBase):
    pass

